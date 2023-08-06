# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         20/12/22 11:48 AM
# Project:      CFHL Transactional Backend
# Module Name:  numeric_code_generator
# Description:
# ****************************************************************
import secrets


def numeric_code_generator(length: int = 6) -> str:
    chars = "1234567890"
    return "".join(secrets.choice(chars) for i in range(length))

