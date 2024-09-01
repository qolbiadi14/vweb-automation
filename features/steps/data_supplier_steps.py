import sys
import os
from behave import given, when, then
from selenium import webdriver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))
from data_supplier_page import DataSupplierPage
from common_steps import *


@then('User berada di halaman data supplier')
def step_user_di_halaman_data_poli(context):
    context.data_supplier_page = DataSupplierPage(context.driver)
    context.data_supplier_page.navigate_to_data_poli()

@when('User klik tombol tambah')
def step_user_klik_tambah(context):
    context.data_supplier_page.click_tambah()

@when('User mengisi field "{field_name}" dengan "{value}"')
def step_user_isi_field(context, field_name, value):
    context.data_supplier_page.fill_field(field_name, value)

@when('User klik tombol simpan')
def step_user_klik_simpan(context):
    context.data_supplier_page.click_simpan()

@then('Data supplier berhasil ditambahkan')
def step_data_supplier_berhasil_ditambahkan(context):
    assert context.data_supplier_page.is_supplier_added()

@then('Data supplier berhasil ditambahkan dengan nama saja')
def step_data_supplier_berhasil_ditambahkan_nama_saja(context):
    assert context.data_supplier_page.is_supplier_added()