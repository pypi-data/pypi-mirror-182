from io import BytesIO, TextIOWrapper


class AzureWriter:
    def __init__(self, account_url, credential, container_name, blob_name,  binary=True) -> None:
        from azure.storage.blob import BlobClient

        self.blob_client = BlobClient(
            account_url=account_url,
            credential=credential,
            container_name=container_name,
            blob_name=blob_name,
        )

        if not self.blob_client.exists():
            self.blob_client.create_append_blob()
        
        self.closed = False
        self.binary = binary

    def write(self, data) -> None:
        if self.binary:
            append_data = memoryview(data)
        else:
            append_data = bytes(data, "utf-8")        
        self.blob_client.append_block(append_data, length=len(append_data))

    def close(self):
        self.closed = True
        self.blob_client.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
        return True


class AzureWriterAIO:
    def __init__(self, account_url, credential, container_name, blob_name, binary=True) -> None:
        from azure.storage.blob.aio import BlobClient

        self.blob_client = BlobClient(
            account_url=account_url,
            credential=credential,
            container_name=container_name,
            blob_name=blob_name,
        )
        self.closed = False
        self.binary = binary

    async def create_append_blob(self, overwrite_existing=False):
        if not await self.blob_client.exists() or overwrite_existing:
            await self.blob_client.create_append_blob()

    async def write(self, data) -> None:
        if self.binary:
            append_data = memoryview(data)
        else:
            append_data = bytes(data, "utf-8")        
        await self.blob_client.append_block(append_data, length=len(append_data))

    async def close(self) -> None:
        await self.blob_client.close()
        self.closed = True

    async def __aenter__(self):
        await self.create_append_blob()
        return self

    async def __aexit__(self, type, value, traceback):
        await self.close()
        return True


class AzureBlobReader:
    def __init__(
        self, account_url, credential, container_name, blob_name, binary=True
    ) -> None:
        from azure.storage.blob import BlobClient

        self.blob_client = BlobClient(
            account_url=account_url,
            credential=credential,
            container_name=container_name,
            blob_name=blob_name,
        )
        self.binary = binary

    def __enter__(self):
        self.in_memory = self.get_file_like_object(binary=self.binary)
        return self

    def __exit__(self, type, value, traceback):
        self.blob_client.close()
        return True

    def get_file_like_object(self):
        download_stream = self.blob_client.download_blob()

        if self.binary:
            in_memory = BytesIO(download_stream.content_as_bytes())
        else:
            in_memory = TextIOWrapper(BytesIO(download_stream.content_as_bytes()))

        return in_memory
