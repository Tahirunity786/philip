-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: hrmsdata
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `pbcatedt`
--

DROP TABLE IF EXISTS `pbcatedt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pbcatedt` (
  `pbe_name` varchar(30) NOT NULL,
  `pbe_edit` varchar(254) DEFAULT NULL,
  `pbe_type` smallint DEFAULT NULL,
  `pbe_cntr` int DEFAULT NULL,
  `pbe_seqn` smallint NOT NULL,
  `pbe_flag` int DEFAULT NULL,
  `pbe_work` char(32) DEFAULT NULL,
  UNIQUE KEY `pbcate_x` (`pbe_name`,`pbe_seqn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pbcatedt`
--

LOCK TABLES `pbcatedt` WRITE;
/*!40000 ALTER TABLE `pbcatedt` DISABLE KEYS */;
INSERT INTO `pbcatedt` VALUES ('###-##-####','###-##-####',90,1,1,32,'00'),('###,###.00','###,###.00',90,1,1,32,'10'),('#####','#####',90,1,1,32,'10'),('DD/MM/YY','DD/MM/YY',90,1,1,32,'20'),('DD/MM/YY HH:MM:SS','DD/MM/YY HH:MM:SS',90,1,1,32,'40'),('DD/MM/YY HH:MM:SS:FFFFFF','DD/MM/YY HH:MM:SS:FFFFFF',90,1,1,32,'40'),('DD/MM/YYYY','DD/MM/YYYY',90,1,1,32,'20'),('DD/MM/YYYY HH:MM:SS','DD/MM/YYYY HH:MM:SS',90,1,1,32,'40'),('DD/MMM/YY','DD/MMM/YY',90,1,1,32,'20'),('DD/MMM/YY HH:MM:SS','DD/MMM/YY HH:MM:SS',90,1,1,32,'40'),('HH:MM:SS','HH:MM:SS',90,1,1,32,'30'),('HH:MM:SS:FFF','HH:MM:SS:FFF',90,1,1,32,'30'),('HH:MM:SS:FFFFFF','HH:MM:SS:FFFFFF',90,1,1,32,'30'),('JJJ/YY','JJJ/YY',90,1,1,32,'20'),('JJJ/YY HH:MM:SS','JJJ/YY HH:MM:SS',90,1,1,32,'40'),('JJJ/YYYY','JJJ/YYYY',90,1,1,32,'20'),('JJJ/YYYY HH:MM:SS','JJJ/YYYY HH:MM:SS',90,1,1,32,'40'),('MM/DD/YY','MM/DD/YY',90,1,1,32,'20'),('MM/DD/YY HH:MM:SS','MM/DD/YY HH:MM:SS',90,1,1,32,'40'),('MM/DD/YYYY','MM/DD/YYYY',90,1,1,32,'20'),('MM/DD/YYYY HH:MM:SS','MM/DD/YYYY HH:MM:SS',90,1,1,32,'40');
/*!40000 ALTER TABLE `pbcatedt` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-16 21:53:05
