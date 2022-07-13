-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: cloudmark
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `presenza`
--

DROP TABLE IF EXISTS `presenza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `presenza` (
  `id_dipendente` int NOT NULL,
  `data` date NOT NULL,
  `tipo_presenza` varchar(45) NOT NULL,
  `id_commessa` int NOT NULL,
  `ore` int DEFAULT NULL,
  PRIMARY KEY (`id_dipendente`,`data`,`tipo_presenza`),
  KEY `tipo_presenza` (`tipo_presenza`),
  KEY `id_commessa` (`id_commessa`),
  CONSTRAINT `presenza_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `dipendente` (`id_dipendente`),
  CONSTRAINT `presenza_ibfk_2` FOREIGN KEY (`tipo_presenza`) REFERENCES `tipo_presenza` (`nome_tipo_presenza`),
  CONSTRAINT `presenza_ibfk_3` FOREIGN KEY (`id_commessa`) REFERENCES `commessa` (`id_commessa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `presenza`
--

LOCK TABLES `presenza` WRITE;
/*!40000 ALTER TABLE `presenza` DISABLE KEYS */;
/*!40000 ALTER TABLE `presenza` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-13 11:08:39
