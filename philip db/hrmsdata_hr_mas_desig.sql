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
-- Table structure for table `hr_mas_desig`
--

DROP TABLE IF EXISTS `hr_mas_desig`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hr_mas_desig` (
  `desig_id` decimal(7,0) NOT NULL,
  `org_id` decimal(7,0) NOT NULL,
  `loc_id` decimal(7,0) NOT NULL,
  `designation` varchar(55) NOT NULL,
  UNIQUE KEY `hr_mas_desig_id` (`desig_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_mas_desig`
--

LOCK TABLES `hr_mas_desig` WRITE;
/*!40000 ALTER TABLE `hr_mas_desig` DISABLE KEYS */;
INSERT INTO `hr_mas_desig` VALUES (1,1833,1,'ACCOUNTS'),(2,1833,1,'ADDL MANAGER'),(3,1833,1,'ADMIN'),(4,1833,1,'ASST. MANAGER -\nPURCHASE'),(5,1833,1,'ASST. OPT.'),(6,1833,1,'ASST.MANAGER'),(7,1833,1,'ASSTT. HR'),(8,1833,1,'CLIENT COORDINATOR'),(9,1833,1,'COSTING EXECUTIVE'),(10,1833,1,'CTP'),(11,1833,1,'D.MANAGER'),(12,1833,1,'DESIGNER'),(13,1833,1,'DIE CUTTING OPT.'),(14,1833,1,'DISPATCH'),(15,1833,1,'DRIVER'),(16,1833,1,'DY. MANAGER -ACCOUNTS'),(17,1833,1,'DY. MANAGER-PURCHASE'),(18,1833,1,'EDP OFFICER'),(19,1833,1,'ELECTRICIAN'),(20,1833,1,'ENGINEER'),(21,1833,1,'EXECUTIVE'),(22,1833,1,'EXECUTIVE-BD'),(23,1833,1,'FEEDERMAN'),(24,1833,1,'FEEDERMAN HB 4C'),(25,1833,1,'FIDDERMAN'),(26,1833,1,'FIELD BOY'),(27,1833,1,'FITTER'),(28,1833,1,'FOR MAN DIE'),(29,1833,1,'FRONT OFFICE EXECUTIVE'),(30,1833,1,'GATHERING'),(31,1833,1,'GENERAL MANAGER \nMAINTENANCE'),(32,1833,1,'GENERAL MANAGER QA,\nQMS & QC'),(33,1833,1,'GRAPHIC DESIGNER'),(34,1833,1,'HEAD'),(35,1833,1,'HEAD COMMERCIAL'),(36,1833,1,'HEAD PPC & SUPPLY CHAIN'),(37,1833,1,'HEAD-NPD'),(38,1833,1,'HELPER'),(39,1833,1,'HELPER ERECTOR'),(40,1833,1,'HONGJING'),(41,1833,1,'HR & ADMIN'),(42,1833,1,'HR EXECUTIVE'),(43,1833,1,'IN-CHARGE'),(44,1833,1,'INCHARGE-LOGISTICS'),(45,1833,1,'INK MATCHING TECHNICIAN'),(46,1833,1,'INKMAN'),(47,1833,1,'INSPECTOR'),(48,1833,1,'INTERNSHIP'),(49,1833,1,'KEY ACCOUNT CORDINATOR'),(50,1833,1,'LAMINATION X 3'),(51,1833,1,'LINE INCHARGE 5 PLY'),(52,1833,1,'LOADER'),(53,1833,1,'LOADING'),(54,1833,1,'MAINT (ELECT)'),(55,1833,1,'MAINT ASST'),(56,1833,1,'MAINTANANCE'),(57,1833,1,'MALI'),(58,1833,1,'MANAGER'),(59,1833,1,'MANAGER -QC'),(60,1833,1,'MANAGER-\nMAINTENANCE'),(61,1833,1,'MANAGER-COST ACCOUNTING'),(62,1833,1,'MGR-ACCOUNTS'),(63,1833,1,'MIS EXECUTIVE'),(64,1833,1,'OFFICE BOY'),(65,1833,1,'OPERATOR'),(66,1833,1,'OPR CUTTING M/C'),(67,1833,1,'OPR ERECTOR'),(68,1833,1,'OPR FOLDING'),(69,1833,1,'OPR PERFECT M/C'),(70,1833,1,'PLATE CLEANING'),(71,1833,1,'PPC'),(72,1833,1,'PRODUCTION HEAD'),(73,1833,1,'PURCHASE\nOFFICER'),(74,1833,1,'QC CHECKER'),(75,1833,1,'QC HAWKINS'),(76,1833,1,'QUALITY SUPERVISOR'),(77,1833,1,'RIDER'),(78,1833,1,'SALES COORDINATIOR'),(79,1833,1,'SCRAP'),(80,1833,1,'SEMI OPERATOR'),(81,1833,1,'SENIOR EXECUTIVE QUALITY'),(82,1833,1,'SENIOR MANAGER\n SUPPLY CHAIN & PLANNING'),(83,1833,1,'SHORTER'),(84,1833,1,'SIDDER'),(85,1833,1,'SORTER'),(86,1833,1,'SR ACCOUNTANT'),(87,1833,1,'SR DESIGNER'),(88,1833,1,'SR PROD SUPERVISOR'),(89,1833,1,'SR. EXECUTIVE'),(90,1833,1,'SR. EXECUTIVE ACCOUNTS'),(91,1833,1,'SR.MANAGER'),(92,1833,1,'STORE ASST.'),(93,1833,1,'STORE EXECUTIVE'),(94,1833,1,'STORE IC'),(95,1833,1,'SUPERVISOR'),(96,1833,1,'SUPERVISOR-\nPRINTING'),(97,1833,1,'SWEEPER'),(98,1833,1,'SYSTEM ADMIN'),(99,1833,1,'V.P'),(100,1833,1,'VARNISH'),(101,1833,1,'VP-SALES'),(102,1833,1,'WELDER'),(103,1833,2,'ACCOUNTS'),(104,1833,2,'ADDL MANAGER'),(105,1833,2,'ADMIN'),(106,1833,2,'ASST. MANAGER -\nPURCHASE'),(107,1833,2,'ASST. OPT.'),(108,1833,2,'ASST.MANAGER'),(109,1833,2,'ASSTT. HR'),(110,1833,2,'CLIENT COORDINATOR'),(111,1833,2,'COSTING EXECUTIVE'),(112,1833,2,'CTP'),(113,1833,2,'D.MANAGER'),(114,1833,2,'DESIGNER'),(115,1833,2,'DIE CUTTING OPT.'),(116,1833,2,'DISPATCH'),(117,1833,2,'DRIVER'),(118,1833,2,'DY. MANAGER -ACCOUNTS'),(119,1833,2,'DY. MANAGER-PURCHASE'),(120,1833,2,'EDP OFFICER'),(121,1833,2,'ELECTRICIAN'),(122,1833,2,'ENGINEER'),(123,1833,2,'EXECUTIVE'),(124,1833,2,'EXECUTIVE-BD'),(125,1833,2,'FEEDERMAN'),(126,1833,2,'FEEDERMAN HB 4C'),(127,1833,2,'FIDDERMAN'),(128,1833,2,'FIELD BOY'),(129,1833,2,'FITTER'),(130,1833,2,'FOR MAN DIE'),(131,1833,2,'FRONT OFFICE EXECUTIVE'),(132,1833,2,'GATHERING'),(133,1833,2,'GENERAL MANAGER \nMAINTENANCE'),(134,1833,2,'GENERAL MANAGER QA,\nQMS & QC'),(135,1833,2,'GRAPHIC DESIGNER'),(136,1833,2,'HEAD'),(137,1833,2,'HEAD COMMERCIAL'),(138,1833,2,'HEAD PPC & SUPPLY CHAIN'),(139,1833,2,'HEAD-NPD'),(140,1833,2,'HELPER'),(141,1833,2,'HELPER ERECTOR'),(142,1833,2,'HONGJING'),(143,1833,2,'HR & ADMIN'),(144,1833,2,'HR EXECUTIVE'),(145,1833,2,'IN-CHARGE'),(146,1833,2,'INCHARGE-LOGISTICS'),(147,1833,2,'INK MATCHING TECHNICIAN'),(148,1833,2,'INKMAN'),(149,1833,2,'INSPECTOR'),(150,1833,2,'INTERNSHIP'),(151,1833,2,'KEY ACCOUNT CORDINATOR'),(152,1833,2,'LAMINATION X 3'),(153,1833,2,'LINE INCHARGE 5 PLY'),(154,1833,2,'LOADER'),(155,1833,2,'LOADING'),(156,1833,2,'MAINT (ELECT)'),(157,1833,2,'MAINT ASST'),(158,1833,2,'MAINTANANCE'),(159,1833,2,'MALI'),(160,1833,2,'MANAGER'),(161,1833,2,'MANAGER -QC'),(162,1833,2,'MANAGER-\nMAINTENANCE'),(163,1833,2,'MANAGER-COST ACCOUNTING'),(164,1833,2,'MGR-ACCOUNTS'),(165,1833,2,'MIS EXECUTIVE'),(166,1833,2,'OFFICE BOY'),(167,1833,2,'OPERATOR'),(168,1833,2,'OPR CUTTING M/C'),(169,1833,2,'OPR ERECTOR'),(170,1833,2,'OPR FOLDING'),(171,1833,2,'OPR PERFECT M/C'),(172,1833,2,'PLATE CLEANING'),(173,1833,2,'PPC'),(174,1833,2,'PRODUCTION HEAD'),(175,1833,2,'PURCHASE\nOFFICER'),(176,1833,2,'QC CHECKER'),(177,1833,2,'QC HAWKINS'),(178,1833,2,'QUALITY SUPERVISOR'),(179,1833,2,'RIDER'),(180,1833,2,'SALES COORDINATIOR'),(181,1833,2,'SCRAP'),(182,1833,2,'SEMI OPERATOR'),(183,1833,2,'SENIOR EXECUTIVE QUALITY'),(184,1833,2,'SENIOR MANAGER\n SUPPLY CHAIN & PLANNING'),(185,1833,2,'SHORTER'),(186,1833,2,'SIDDER'),(187,1833,2,'SORTER'),(188,1833,2,'SR ACCOUNTANT'),(189,1833,2,'SR DESIGNER'),(190,1833,2,'SR PROD SUPERVISOR'),(191,1833,2,'SR. EXECUTIVE'),(192,1833,2,'SR. EXECUTIVE ACCOUNTS'),(193,1833,2,'SR.MANAGER'),(194,1833,2,'STORE ASST.'),(195,1833,2,'STORE EXECUTIVE'),(196,1833,2,'STORE IC'),(197,1833,2,'SUPERVISOR'),(198,1833,2,'SUPERVISOR-\nPRINTING'),(199,1833,2,'SWEEPER'),(200,1833,2,'SYSTEM ADMIN'),(201,1833,2,'V.P'),(202,1833,2,'VARNISH'),(203,1833,2,'VP-SALES'),(204,1833,2,'WELDER'),(205,1833,3,'ACCOUNTS'),(206,1833,3,'ADDL MANAGER'),(207,1833,3,'ADMIN'),(208,1833,3,'ASST. MANAGER -\nPURCHASE'),(209,1833,3,'ASST. OPT.'),(210,1833,3,'ASST.MANAGER'),(211,1833,3,'ASSTT. HR'),(212,1833,3,'CLIENT COORDINATOR'),(213,1833,3,'COSTING EXECUTIVE'),(214,1833,3,'CTP'),(215,1833,3,'D.MANAGER'),(216,1833,3,'DESIGNER'),(217,1833,3,'DIE CUTTING OPT.'),(218,1833,3,'DISPATCH'),(219,1833,3,'DRIVER'),(220,1833,3,'DY. MANAGER -ACCOUNTS'),(221,1833,3,'DY. MANAGER-PURCHASE'),(222,1833,3,'EDP OFFICER'),(223,1833,3,'ELECTRICIAN'),(224,1833,3,'ENGINEER'),(225,1833,3,'EXECUTIVE'),(226,1833,3,'EXECUTIVE-BD'),(227,1833,3,'FEEDERMAN'),(228,1833,3,'FEEDERMAN HB 4C'),(229,1833,3,'FIDDERMAN'),(230,1833,3,'FIELD BOY'),(231,1833,3,'FITTER'),(232,1833,3,'FOR MAN DIE'),(233,1833,3,'FRONT OFFICE EXECUTIVE'),(234,1833,3,'GATHERING'),(235,1833,3,'GENERAL MANAGER \nMAINTENANCE'),(236,1833,3,'GENERAL MANAGER QA,\nQMS & QC'),(237,1833,3,'GRAPHIC DESIGNER'),(238,1833,3,'HEAD'),(239,1833,3,'HEAD COMMERCIAL'),(240,1833,3,'HEAD PPC & SUPPLY CHAIN'),(241,1833,3,'HEAD-NPD'),(242,1833,3,'HELPER'),(243,1833,3,'HELPER ERECTOR'),(244,1833,3,'HONGJING'),(245,1833,3,'HR & ADMIN'),(246,1833,3,'HR EXECUTIVE'),(247,1833,3,'IN-CHARGE'),(248,1833,3,'INCHARGE-LOGISTICS'),(249,1833,3,'INK MATCHING TECHNICIAN'),(250,1833,3,'INKMAN'),(251,1833,3,'INSPECTOR'),(252,1833,3,'INTERNSHIP'),(253,1833,3,'KEY ACCOUNT CORDINATOR'),(254,1833,3,'LAMINATION X 3'),(255,1833,3,'LINE INCHARGE 5 PLY'),(256,1833,3,'LOADER'),(257,1833,3,'LOADING'),(258,1833,3,'MAINT (ELECT)'),(259,1833,3,'MAINT ASST'),(260,1833,3,'MAINTANANCE'),(261,1833,3,'MALI'),(262,1833,3,'MANAGER'),(263,1833,3,'MANAGER -QC'),(264,1833,3,'MANAGER-\nMAINTENANCE'),(265,1833,3,'MANAGER-COST ACCOUNTING'),(266,1833,3,'MGR-ACCOUNTS'),(267,1833,3,'MIS EXECUTIVE'),(268,1833,3,'OFFICE BOY'),(269,1833,3,'OPERATOR'),(270,1833,3,'OPR CUTTING M/C'),(271,1833,3,'OPR ERECTOR'),(272,1833,3,'OPR FOLDING'),(273,1833,3,'OPR PERFECT M/C'),(274,1833,3,'PLATE CLEANING'),(275,1833,3,'PPC'),(276,1833,3,'PRODUCTION HEAD'),(277,1833,3,'PURCHASE\nOFFICER'),(278,1833,3,'QC CHECKER'),(279,1833,3,'QC HAWKINS'),(280,1833,3,'QUALITY SUPERVISOR'),(281,1833,3,'RIDER'),(282,1833,3,'SALES COORDINATIOR'),(283,1833,3,'SCRAP'),(284,1833,3,'SEMI OPERATOR'),(285,1833,3,'SENIOR EXECUTIVE QUALITY'),(286,1833,3,'SENIOR MANAGER\n SUPPLY CHAIN & PLANNING'),(287,1833,3,'SHORTER'),(288,1833,3,'SIDDER'),(289,1833,3,'SORTER'),(290,1833,3,'SR ACCOUNTANT'),(291,1833,3,'SR DESIGNER'),(292,1833,3,'SR PROD SUPERVISOR'),(293,1833,3,'SR. EXECUTIVE'),(294,1833,3,'SR. EXECUTIVE ACCOUNTS'),(295,1833,3,'SR.MANAGER'),(296,1833,3,'STORE ASST.'),(297,1833,3,'STORE EXECUTIVE'),(298,1833,3,'STORE IC'),(299,1833,3,'SUPERVISOR'),(300,1833,3,'SUPERVISOR-\nPRINTING'),(301,1833,3,'SWEEPER'),(302,1833,3,'SYSTEM ADMIN'),(303,1833,3,'V.P'),(304,1833,3,'VARNISH'),(305,1833,3,'VP-SALES'),(306,1833,3,'WELDER');
/*!40000 ALTER TABLE `hr_mas_desig` ENABLE KEYS */;
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
