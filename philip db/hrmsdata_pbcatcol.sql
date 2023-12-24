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
-- Table structure for table `pbcatcol`
--

DROP TABLE IF EXISTS `pbcatcol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pbcatcol` (
  `pbc_tnam` char(193) NOT NULL,
  `pbc_tid` int DEFAULT NULL,
  `pbc_ownr` char(193) NOT NULL,
  `pbc_cnam` char(193) NOT NULL,
  `pbc_cid` smallint DEFAULT NULL,
  `pbc_labl` varchar(254) DEFAULT NULL,
  `pbc_lpos` smallint DEFAULT NULL,
  `pbc_hdr` varchar(254) DEFAULT NULL,
  `pbc_hpos` smallint DEFAULT NULL,
  `pbc_jtfy` smallint DEFAULT NULL,
  `pbc_mask` varchar(31) DEFAULT NULL,
  `pbc_case` smallint DEFAULT NULL,
  `pbc_hght` smallint DEFAULT NULL,
  `pbc_wdth` smallint DEFAULT NULL,
  `pbc_ptrn` varchar(31) DEFAULT NULL,
  `pbc_bmap` char(1) DEFAULT NULL,
  `pbc_init` varchar(254) DEFAULT NULL,
  `pbc_cmnt` varchar(254) DEFAULT NULL,
  `pbc_edit` varchar(31) DEFAULT NULL,
  `pbc_tag` varchar(254) DEFAULT NULL,
  UNIQUE KEY `pbcatc_x` (`pbc_tnam`,`pbc_ownr`,`pbc_cnam`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pbcatcol`
--

LOCK TABLES `pbcatcol` WRITE;
/*!40000 ALTER TABLE `pbcatcol` DISABLE KEYS */;
INSERT INTO `pbcatcol` VALUES ('hr_emps',NULL,'root','active',NULL,NULL,0,NULL,0,23,NULL,0,61,69,NULL,'N',NULL,NULL,NULL,NULL),('hr_emps',NULL,'root','lastpdate',NULL,NULL,0,NULL,0,23,NULL,0,61,188,NULL,'N',NULL,NULL,NULL,NULL),('hr_emps',NULL,'root','loginpw',NULL,NULL,0,NULL,0,23,NULL,0,61,485,NULL,'N',NULL,NULL,NULL,NULL),('hr_emps',NULL,'root','oldcodeno',NULL,NULL,0,NULL,0,23,NULL,0,61,261,NULL,'N',NULL,NULL,NULL,NULL),('hr_emps',NULL,'root','otdivhrs',NULL,NULL,0,NULL,0,24,'[General]',0,61,206,NULL,'N',NULL,NULL,NULL,NULL),('hr_emps',NULL,'root','otsh',NULL,NULL,0,NULL,0,23,NULL,0,61,69,NULL,'N',NULL,NULL,NULL,NULL),('hr_mas_desig',NULL,'root','desig_id',NULL,NULL,0,NULL,0,24,'[General]',0,61,206,NULL,'N',NULL,NULL,NULL,NULL),('hr_mas_desig',NULL,'root','designation',NULL,NULL,0,NULL,0,23,NULL,0,61,1006,NULL,'N',NULL,NULL,NULL,NULL),('hr_mas_desig',NULL,'root','loc_id',NULL,NULL,0,NULL,0,24,'[General]',0,61,206,NULL,'N',NULL,NULL,NULL,NULL),('hr_mas_desig',NULL,'root','org_id',NULL,NULL,0,NULL,0,24,'[General]',0,61,206,NULL,'N',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `pbcatcol` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-16 21:53:06
