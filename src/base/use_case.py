import logging

from .exception import BaseFinanceException

logger = logging.getLogger(__name__)


class BaseUseCaseRequest(object):
    """Base class of Request for UseCase"""

    def __init__(self):
        self.errors = []

    def add_error(self, error: Exception) -> None:
        self.errors.append(error)

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __nonzero__(self) -> bool:
        return not self.has_errors()

    def is_valid(self, *args, **kwargs):
        return self

    def __iter__(self):
        for k, v in self.__dict__.items():
            yield k, v

    __bool__ = __nonzero__


class BaseUseCaseResponse(object):
    """Base class of Response for UseCase"""

    def __init__(self, value=None, *args, **kwargs):
        self.errors = []
        self.value = value

    def add_error(self, error: Exception) -> None:
        self.errors.append(error)

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def __nonzero__(self) -> bool:
        return not self.has_errors()

    __bool__ = __nonzero__

    def get_display_error_message(self, *args, **kwargs) -> dict:
        """
        Get user's message of exceptions
        """

        errors = []
        for error in self.errors:
            errors.append({
                'message': str(getattr(error, 'message', str(error))).lower(),
                'error_code': getattr(error, 'error_code', 0),
                'http_code': getattr(error, 'http_code', [])
            })
        return {
            "errors_occured": errors
        }

    def get_first_error_message(self) -> str:
        """ Get first error message """
        error_message = self.get_display_error_message()
        return error_message['errors_occured'][0]['message']

    @classmethod
    def build_from_exception(cls, exception: Exception):
        """Build instance of class for response from error """
        if not issubclass(type(exception), BaseFinanceException):
            exception = BaseFinanceException()
        instance = cls()
        instance.errors.extend([exception])
        return instance

    @classmethod
    def build_from_invalid_request(cls, invalid_request: 'BaseUseCaseRequest') -> 'BaseUseCaseResponse':
        """Build instance of class for response from invalid request """
        instance = cls()
        instance.errors.extend(invalid_request.errors)
        return instance


class BaseUseCase:
    """Base UseCase """

    async def execute(self, request: BaseUseCaseRequest, *args, **kwargs) -> BaseUseCaseResponse:
        request = request.is_valid()
        if bool(request):
            try:
                response = await self.__execute__(request)
            except Exception as e:
                logger.exception('Unhandled use_case error:{}'.format(str(e)))
                response = BaseUseCaseResponse.build_from_exception(e)
        else:
            response = BaseUseCaseResponse.build_from_invalid_request(request)
        return response

    async def __execute__(self, request: BaseUseCaseRequest, *args, **kwargs) -> BaseUseCaseResponse:
        """Method for main business logic """
        raise NotImplementedError()
