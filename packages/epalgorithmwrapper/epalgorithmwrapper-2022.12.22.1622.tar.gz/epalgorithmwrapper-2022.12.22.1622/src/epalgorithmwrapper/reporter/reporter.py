from logging import Logger

class Reporter:
    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    def _print(self, message):
        self._logger.info(message)
    
    def open(self) -> "Reporter":
        return self
    
    def close(self):
        return
        
    def report(self, message: str) -> bool:
        raise NotImplementedError
    
    def __enter__(self):
        return self.open()
    
    def __exit__(self, type, value, tb):
        return self.close()

class ReporterConnectionDetails:
    def __init__(self,
            host,
            creds_provider = None,
            messagebus = None) -> None:
        self.host = host
        self.creds_provider = creds_provider
        self.messagebus = messagebus