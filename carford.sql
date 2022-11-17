-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: carford
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `tbcarro`
--

DROP TABLE IF EXISTS `tbcarro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbcarro` (
  `id_proprietario` int NOT NULL,
  `id_carro` int NOT NULL AUTO_INCREMENT,
  `placa` varchar(8) COLLATE utf8_bin DEFAULT NULL,
  `descricao` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `modelo` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `cor` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `situacao` varchar(1) COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`id_carro`,`id_proprietario`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbcarro`
--

LOCK TABLES `tbcarro` WRITE;
/*!40000 ALTER TABLE `tbcarro` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbcarro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tbproprietario`
--

DROP TABLE IF EXISTS `tbproprietario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbproprietario` (
  `id_proprietario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) COLLATE utf8_bin DEFAULT NULL,
  `logradouro` varchar(60) COLLATE utf8_bin DEFAULT NULL,
  `numero` int DEFAULT NULL,
  `telefone` varchar(15) COLLATE utf8_bin DEFAULT NULL,
  `possui_carro` varchar(1) COLLATE utf8_bin DEFAULT NULL,
  `situacao` varchar(1) COLLATE utf8_bin DEFAULT NULL,
  `qtde_carros` int DEFAULT NULL,
  PRIMARY KEY (`id_proprietario`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbproprietario`
--

LOCK TABLES `tbproprietario` WRITE;
/*!40000 ALTER TABLE `tbproprietario` DISABLE KEYS */;
INSERT INTO `tbproprietario` VALUES (1,'CarFord','Rod. José Carlos Daux',8600,'(48)3206-0265','N','A',0);
/*!40000 ALTER TABLE `tbproprietario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-16 23:32:27
