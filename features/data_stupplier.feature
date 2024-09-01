Feature: Tambah Data supplier

  Scenario: Tambah data supplier dengan semua field terisi
    When User klik tombol tambah
    And User mengisi field nama supplier
    And User mengisi field alamat
    And User mengisi field kota
    And User mengisi field No.hp
    And User mengisi field telepon
    And User mengisi field no rekening
    And User mengisi field NPWP
    And User klik tombol simpan
    Then Data supplier berhasil ditambahkan

  Scenario: Tambah data supplier dengan hanya field nama terisi
    When User klik tombol tambah
    And User mengisi field nama supplier
    And User klik tombol simpan
    Then Data supplier berhasil ditambahkan dengan nama saja
