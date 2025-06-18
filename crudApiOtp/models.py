# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authentication2Af(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10)
    document = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    state = models.IntegerField()
    validate_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'authentication_2af'


class Banks(models.Model):
    id = models.BigAutoField(primary_key=True)
    financialinstitutioncode = models.CharField(db_column='financialInstitutionCode', max_length=255)  # Field name made lowercase.
    financialinstitutionname = models.CharField(db_column='financialInstitutionName', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    format = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banks'


class Companies(models.Model):
    id = models.BigAutoField(primary_key=True)
    entity_code = models.CharField(max_length=255, db_comment='Campo que registra el nit de la empresa')
    client_id = models.CharField(max_length=255, db_comment='Campo que registra el codigo del cliente dado por ach')
    client_secret = models.CharField(max_length=255, db_comment='Campo que registra codigo secreto dado por ach')
    entity_name = models.CharField(max_length=255, db_comment='Nombre de la entidad.')
    type_entity = models.CharField(max_length=255, db_comment='Tipo de entidad 01 para natural, 02 para juridica')
    type_document = models.CharField(max_length=255, db_comment='Tipo de documento en este caso NIT.')
    number_document = models.CharField(max_length=255, db_comment='Numero de nit')
    ciiu = models.CharField(max_length=255, db_comment='Codigo ciiu referenciado por el dane.')
    encryption_key = models.CharField(max_length=255, db_comment='Llave de cifrado simetrico AES 256 bits')
    iv_key = models.CharField(max_length=255, db_comment='IV de cifrado simetrico AES 256 bits')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    format = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class LogErrorPays(models.Model):
    id = models.BigAutoField(primary_key=True)
    document = models.CharField(max_length=255, db_comment='Documento del cliente.')
    obligation = models.CharField(max_length=255, db_comment='Obligacion del cliente.')
    cartera = models.CharField(max_length=255, db_comment='Key de la cartera donde esta la deuda.')
    trazabilitycode = models.IntegerField(db_column='trazabilityCode', db_comment='Codigo de la transaccion.')  # Field name made lowercase.
    errors = models.JSONField(db_comment='Json que almacena los errores.')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_error_pays'


class LogResponses(models.Model):
    id = models.BigAutoField(primary_key=True)
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    request_parameters = models.JSONField(db_comment='campo que guarda toda la data de la peticion')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_responses'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class NoSupportedCarteras(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_cartera = models.CharField(max_length=255)
    state = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'no_supported_carteras'


class Pays(models.Model):
    id = models.BigAutoField(primary_key=True)
    document = models.CharField(max_length=255, db_comment='Campo que registra el documento del cliente.')
    obligation = models.CharField(max_length=255, db_comment='Campo que registra el numero de obligacion que pagaron')
    transaction_state = models.CharField(max_length=255, blank=True, null=True, db_comment='Campo que registra el estado de la transaccion')
    authorization_id = models.CharField(max_length=255, blank=True, null=True, db_comment='Campo que registra el numero de autorizacion')
    amount_pay = models.CharField(max_length=255, db_comment='Campo que registra monto pagado')
    key_cartera = models.CharField(max_length=255, db_comment='Campo que registra monto pagado')
    trazabilitycode = models.CharField(db_column='trazabilityCode', unique=True, max_length=255, db_comment='Codigo de la transaccion.')  # Field name made lowercase.
    payment_applied = models.IntegerField(db_comment='Campo que registra si ya se aplico el pago a la cartera')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    bank_name = models.CharField(max_length=255, db_comment='Nombre del banco de la cartera donde se aplica el pago.')
    agreement = models.CharField(max_length=255, db_comment='Convenio del banco')
    method = models.CharField(max_length=255, db_comment='Metodo de pago')
    ticketid = models.CharField(db_column='ticketId', max_length=255, db_comment='Numero de factura que se genera para el pago.')  # Field name made lowercase.
    format = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pays'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class Secret2Af(models.Model):
    id = models.BigAutoField(primary_key=True)
    secret_key = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secret_2af'


class ServiceCodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    service_code = models.CharField(max_length=255)
    account = models.CharField(max_length=255, db_comment='Cuenta relacionada al codigo de servicio')
    type_account = models.CharField(max_length=255, db_comment='Tipo de cuenta')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    format = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'service_codes'


class Tokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    seconds = models.CharField(max_length=255)
    generation_date = models.DateField()
    generation_hour = models.TimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    format = models.IntegerField(blank=True, null=True, db_comment='Campo de Identificacion de empresa')

    class Meta:
        managed = False
        db_table = 'tokens'


class TypeDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_documents'


class TypeUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_users'
