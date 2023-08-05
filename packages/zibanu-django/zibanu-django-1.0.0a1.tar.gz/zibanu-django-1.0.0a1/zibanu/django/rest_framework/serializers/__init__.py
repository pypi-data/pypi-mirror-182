# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         13/12/22 7:39 AM
# Project:      CFHL Transactional Backend
# Module Name:  __init__.py
# Description:
# ****************************************************************
from .model_serializer import ModelSerializer
from rest_framework.serializers import *

__all__ = [
    "ModelSerializer",
]

