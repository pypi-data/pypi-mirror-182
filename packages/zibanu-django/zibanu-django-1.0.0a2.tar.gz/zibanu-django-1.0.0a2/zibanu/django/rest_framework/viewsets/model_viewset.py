# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         19/12/22 3:18 PM
# Project:      CFHL Transactional Backend
# Module Name:  model_viewset
# Description:
# ****************************************************************
from django.db import DatabaseError
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import QuerySet
from rest_framework.viewsets import ModelViewSet as RestModelViewSet
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from zibanu.django.rest_framework.exceptions import APIException
from zibanu.django.rest_framework.exceptions import ValidationError
from zibanu.django.utils import ErrorMessages


class ModelViewSet(RestModelViewSet):
    """
    Override ModelViewSet class for default Zibanu functionality
    """
    model = None
    http_method_names = ["post"]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTTokenUserAuthentication]

    if settings.DEBUG:
        authentication_classes.append(authentication.TokenAuthentication)

    def get_queryset(self, **kwargs) -> QuerySet:
        """
        Method to get a queryset from model
        :param kwargs: kwargs used for filter and build a queryset
        :return: queryset
        """
        pk = kwargs.get("pk", None)
        qs = self.model.objects.get_queryset()
        if pk is not None:
            qs = qs.filter(pk=pk)
        elif len(kwargs) > 0:
            qs = qs.filter(**kwargs)
        else:
            qs = qs.all()

        return qs

    def list(self, request, *args, **kwargs) -> Response:
        """
        Base method to list the items from model
        :param request: request object from HTTP
        :param args: args data from request
        :param kwargs: args dict from request
        :return: response object
        """
        try:
            serializer = self.get_serializer(instance=self.get_queryset(), many=True)
            data_return = serializer.data
            status_return = status.HTTP_200_OK if len(data_return) > 0 else status.HTTP_204_NO_CONTENT
            data_return = data_return
        except APIException as exc:
            raise APIException(msg=exc.detail.get("message"), error=exc.detail.get("detail"),
                               http_status=exc.status_code) from exc
        except Exception as exc:
            raise APIException(error=str(exc), http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(data=data_return, status=status_return)

    def retrieve(self, request, *args, **kwargs) -> Response:
        """
        Method to get an object or objects based on id or pk
        :param request: request object from HTTP
        :param args: args data from request
        :param kwargs: args dict from request
        :return: response object
        """
        try:
            if "pk" in request.data.keys():
                pk = request.data.get("pk")
            elif "id" in request.data.keys():
                pk = request.data.get("id")
            else:
                raise APIException(ErrorMessages.DATA_REQUIRED, "get", status.HTTP_406_NOT_ACCEPTABLE)

            data_record = self.get_queryset(pk=pk).get()
            data_return = self.get_serializer(data=data_record).data
            status_return = status.HTTP_200_OK
        except ObjectDoesNotExist as exc:
            raise APIException(ErrorMessages.NOT_FOUND, str(exc), http_status=status.HTTP_404_NOT_FOUND) from exc
        except APIException as exc:
            raise APIException(exc.detail.get("message"), exc.detail.get("detail"), exc.status_code) from exc
        except Exception as exc:
            raise APIException(error=str(exc), http_status=status.HTTP_500_INTERNAL_SERVER_ERROR) from exc
        else:
            return Response(status=status_return, data=data_return)

    def get(self, request, *args, **kwargs) -> Response:
        """
        Legacy method for migration purpose
        :param request: request object from HTTP
        :param args: args data from request
        :param kwargs: args dict from request
        :return: response object
        """
        return self.retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs) -> Response:
        """
        Base method to create an instance of entity
        :param request: request object from HTTP
        :param args: args data from request
        :param kwargs: args dict from request
        :return: response object
        """
        try:
            data_return = []
            status_return = status.HTTP_400_BAD_REQUEST
            request_data = request.data
            if len(request_data) > 0:
                serializer = self.get_serializer(data=request_data)
                if serializer.is_valid(raise_exception=True):
                    created = serializer.create(validated_data=serializer.validated_data)
                    if created is not None:
                        data_return = self.get_serializer(created).data
                        status_return = status.HTTP_201_CREATED
                    else:
                        raise ValidationError(ErrorMessages.CREATE_ERROR, "create")
            else:
                raise APIException(ErrorMessages.DATA_REQUIRED)
        except DatabaseError as exc:
            raise APIException(ErrorMessages.DATABASE_ERROR, str(exc)) from exc
        except ValidationError as exc:
            raise APIException(error=str(exc.detail), http_status=status.HTTP_406_NOT_ACCEPTABLE) from exc
        except APIException as exc:
            raise APIException(exc.detail.get("message"), exc.detail.get("detail"), exc.status_code) from exc
        except Exception as exc:
            raise APIException(error=str(exc), http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status_return, data=data_return)
