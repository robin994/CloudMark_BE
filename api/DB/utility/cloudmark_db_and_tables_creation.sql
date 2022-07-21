CREATE DATABASE IF NOT EXISTS CloudMark;

USE CloudMark;

DROP TABLE IF EXISTS `azienda`;
CREATE TABLE `azienda` (
  `id_azienda` varchar(80) NOT NULL,
  `nome` varchar(90) DEFAULT NULL,
  `p_iva` char(11) DEFAULT NULL,
  `indirizzo` varchar(90) DEFAULT NULL,
  `cap` char(5) DEFAULT NULL,
  `iban` char(27) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `pec` varchar(45) DEFAULT NULL,
  `fax` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_azienda`),
  UNIQUE KEY `nome_UNIQUE` (`nome`)
);

DROP TABLE IF EXISTS `cliente`;
CREATE TABLE `cliente` (
  `id_cliente` varchar(80) NOT NULL ,
  `nome` varchar(90) DEFAULT NULL,
  `p_iva` char(11) DEFAULT NULL,
  `indirizzo` varchar(90) DEFAULT NULL,
  `cap` char(5) DEFAULT NULL,
  `iban` char(27) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  `pec` varchar(90) DEFAULT NULL,
  `fax` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
);

DROP TABLE IF EXISTS `tipo_contratto`;
CREATE TABLE `tipo_contratto` (
  `id_tipo_contratto` varchar(80) NOT NULL,
  `nome_tipo_contratto` varchar(45) NOT NULL,
  `descrizione` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_tipo_contratto`, `nome_tipo_contratto`)
);

DROP TABLE IF EXISTS `dipendente`;
CREATE TABLE `dipendente` (
  `id_dipendente` varchar(80) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `cognome` varchar(45) DEFAULT NULL,
  `cf` varchar(16) NOT NULL,
  `iban` varchar(45) NOT NULL,
  `id_tipo_contratto` varchar(80) NOT NULL,
  `email` varchar(90) DEFAULT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_dipendente`),
  UNIQUE KEY `cf_UNIQUE` (`cf`),
  KEY `tipo_contratto_idx` (`id_tipo_contratto`),
  KEY `fk_dipendente_tipo_contratto_idx` (`id_tipo_contratto`),
  CONSTRAINT `dipendente_ibfk_1` FOREIGN KEY (`id_tipo_contratto`) REFERENCES `tipo_contratto` (`id_tipo_contratto`)
);

DROP TABLE IF EXISTS `tipo_account`;
CREATE TABLE `tipo_account` (
  `id_tipo_account` int NOT NULL AUTO_INCREMENT,
  `nome_tipo_account` varchar(45) NOT NULL,
  `lista_funzioni_del_profilo` text,
  PRIMARY KEY (`id_tipo_account`)
);


DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id_account` varchar(80) NOT NULL,
  `user` varchar(45) NOT NULL,
  `password` VARBINARY(64) NOT NULL,
  `abilitato` tinyint(1) DEFAULT NULL,
  `id_tipo_account` int NOT NULL,
  PRIMARY KEY (`id_account`),
  UNIQUE KEY `user_UNIQUE` (`user`),
  KEY `id_tipoAccount` (`id_tipo_account`),
  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`id_tipo_account`) REFERENCES `tipo_account` (`id_tipo_account`)
);

DROP TABLE IF EXISTS `commessa`;
CREATE TABLE `commessa` (
  `id_commessa` varchar(80) NOT NULL,
  `descrizione` varchar(255) DEFAULT NULL,
  `id_cliente` varchar(120) NOT NULL,
  `id_azienda` varchar(80) NOT NULL,
  `data_inizio` date NOT NULL,
  `data_fine` date NOT NULL,
  PRIMARY KEY (`id_commessa`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_azienda` (`id_azienda`),
  CONSTRAINT `commessa_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`),
  CONSTRAINT `commessa_ibfk_2` FOREIGN KEY (`id_azienda`) REFERENCES `azienda` (`id_azienda`)
);

DROP TABLE IF EXISTS `tipo_presenza`;
CREATE TABLE `tipo_presenza` (
  `id_tipo_presenza` int NOT NULL AUTO_INCREMENT,
  `nome_tipo_presenza` varchar(45) NOT NULL,
  `perc_maggiorazione_paga_oraria` int DEFAULT NULL,
  `paga_oraria` int DEFAULT NULL,
  PRIMARY KEY (`id_tipo_presenza`)
);

DROP TABLE IF EXISTS `presenza`;
CREATE TABLE `presenza` (
  `id_presenza` varchar(80) NOT NULL,
  `id_dipendente`varchar(80) NOT NULL,
  `data` date NOT NULL,
  `id_tipo_presenza` int NOT NULL,
  `id_commessa` varchar(80) NOT NULL,
  `ore` int DEFAULT NULL,
  PRIMARY KEY (`id_presenza`,`id_dipendente`),
  KEY `id_dipendente` (`id_dipendente`),
  CONSTRAINT `presenza_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`),
  CONSTRAINT `presenza_ibfk_2` FOREIGN KEY (`id_tipo_presenza`) REFERENCES `tipo_presenza` (`id_tipo_presenza`),
  CONSTRAINT `presenza_ibfk_3` FOREIGN KEY (`id_commessa`) REFERENCES `commessa` (`id_commessa`)
);

DROP TABLE IF EXISTS `account_dipendente`;
CREATE TABLE `account_dipendente` (
  `id_account` varchar(80) NOT NULL,
  `id_dipendente` varchar(80) NOT NULL,
  PRIMARY KEY (`id_dipendente`,`id_account`),
  KEY `id_account` (`id_account`),
  CONSTRAINT `account_dipendente_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`),
  CONSTRAINT `account_dipendente_ibfk_2` FOREIGN KEY (`id_account`) REFERENCES `account` (`id_account`)
);

DROP TABLE IF EXISTS `azienda_cliente`;
CREATE TABLE `azienda_cliente` (
  `id_azienda` varchar(80) NOT NULL,
  `id_cliente` varchar(80) NOT NULL,
  PRIMARY KEY (`id_azienda`,`id_cliente`),
  KEY `id_cliente` (`id_cliente`),
  CONSTRAINT `azienda_cliente_ibfk_1` FOREIGN KEY (`id_azienda`) REFERENCES `azienda` (`id_azienda`),
  CONSTRAINT `azienda_cliente_ibfk_2` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`)
);

DROP TABLE IF EXISTS `commessa_dipendente`;
CREATE TABLE `commessa_dipendente` (
  `id_commessa` varchar(80) NOT NULL,
  `id_dipendente` varchar(80) NOT NULL,
  `rate` decimal(10,0) NOT NULL,
  PRIMARY KEY (`id_commessa`,`id_dipendente`),
  KEY `id_dipendente` (`id_dipendente`),
  CONSTRAINT `commessa_dipendente_ibfk_1` FOREIGN KEY (`id_commessa`) REFERENCES `commessa` (`id_commessa`),
  CONSTRAINT `commessa_dipendente_ibfk_2` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`)
);

DROP TABLE IF EXISTS `dipendente_azienda`;
CREATE TABLE `dipendente_azienda` (
  `id_dipendente` varchar(80) NOT NULL,
  `id_azienda` varchar(80) NOT NULL,
  `data_inizio_rapporto` date NOT NULL,
  `matricola` varchar(45) DEFAULT NULL,
  `data_fine_rapporto` date DEFAULT NULL,
  PRIMARY KEY (`id_dipendente`,`id_azienda`),
  UNIQUE KEY `matricola_UNIQUE` (`matricola`),
  KEY `id_azienda` (`id_azienda`),
  CONSTRAINT `dipendente_azienda_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`),
  CONSTRAINT `dipendente_azienda_ibfk_2` FOREIGN KEY (`id_azienda`) REFERENCES `azienda` (`id_azienda`)
);

DROP TABLE IF EXISTS `saltini`;
CREATE TABLE `saltini` (
  `id_account` varchar(80) NOT NULL,
  `salt` VARBINARY(64) NOT NULL,
  PRIMARY KEY (`id_account`),
  KEY `id_account` (`id_account`),
  CONSTRAINT `saltini_ibfk_1` FOREIGN KEY (`id_account`) REFERENCES `account` (`id_account`) ON DELETE CASCADE
);

