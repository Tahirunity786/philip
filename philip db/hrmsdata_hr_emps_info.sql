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
-- Table structure for table `hr_emps_info`
--

DROP TABLE IF EXISTS `hr_emps_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hr_emps_info` (
  `empid` decimal(10,0) NOT NULL,
  `nationallity` varchar(20) DEFAULT NULL,
  `religion` varchar(3) DEFAULT NULL,
  `pancardno` varchar(25) DEFAULT NULL,
  `voteridno` varchar(25) DEFAULT NULL,
  `dvlicenceno` varchar(25) DEFAULT NULL,
  `passportno` varchar(25) DEFAULT NULL,
  `docno` varchar(25) DEFAULT NULL,
  `pricontactno` varchar(25) DEFAULT NULL,
  `seccontactno` varchar(25) DEFAULT NULL,
  `address1` varchar(55) DEFAULT NULL,
  `address2` varchar(55) DEFAULT NULL,
  `address3` varchar(55) DEFAULT NULL,
  `city` varchar(55) DEFAULT NULL,
  `state` varchar(55) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `peaddress1` varchar(55) DEFAULT NULL,
  `peaddress2` varchar(55) DEFAULT NULL,
  `peaddress3` varchar(55) DEFAULT NULL,
  `pecity` varchar(55) DEFAULT NULL,
  `pestate` varchar(55) DEFAULT NULL,
  `pepincode` varchar(10) DEFAULT NULL,
  `languesknown` varchar(70) DEFAULT NULL,
  `height` varchar(20) DEFAULT NULL,
  `weight` varchar(20) DEFAULT NULL,
  `idmark` varchar(40) DEFAULT NULL,
  `langspeak` varchar(55) DEFAULT NULL,
  `langread` varchar(55) DEFAULT NULL,
  `langwrite` varchar(55) DEFAULT NULL,
  `educat1` varchar(55) DEFAULT NULL,
  `educat1year` varchar(10) DEFAULT NULL,
  `educat1div` varchar(10) DEFAULT NULL,
  `educat1per` varchar(10) DEFAULT NULL,
  `educat2` varchar(55) DEFAULT NULL,
  `educat2year` varchar(10) DEFAULT NULL,
  `educat2div` varchar(10) DEFAULT NULL,
  `educat2per` varchar(10) DEFAULT NULL,
  `educat3` varchar(55) DEFAULT NULL,
  `educat3year` varchar(10) DEFAULT NULL,
  `educat3div` varchar(10) DEFAULT NULL,
  `educat3per` varchar(10) DEFAULT NULL,
  `educat4` varchar(55) DEFAULT NULL,
  `educat4year` varchar(10) DEFAULT NULL,
  `educat4div` varchar(10) DEFAULT NULL,
  `educat4per` varchar(10) DEFAULT NULL,
  `educat5` varchar(55) DEFAULT NULL,
  `educat5year` varchar(10) DEFAULT NULL,
  `educat5div` varchar(10) DEFAULT NULL,
  `educat5per` varchar(10) DEFAULT NULL,
  `educat6` varchar(55) DEFAULT NULL,
  `educat6year` varchar(10) DEFAULT NULL,
  `educat6div` varchar(10) DEFAULT NULL,
  `educat6per` varchar(10) DEFAULT NULL,
  `educat7` varchar(55) DEFAULT NULL,
  `educat7year` varchar(10) DEFAULT NULL,
  `educat7div` varchar(10) DEFAULT NULL,
  `educat7per` varchar(10) DEFAULT NULL,
  `totalexperience` varchar(10) DEFAULT NULL,
  `employer1` varchar(55) DEFAULT NULL,
  `post1` varchar(30) DEFAULT NULL,
  `fromto1` varchar(20) DEFAULT NULL,
  `reason1` varchar(20) DEFAULT NULL,
  `employer2` varchar(55) DEFAULT NULL,
  `post2` varchar(30) DEFAULT NULL,
  `fromto2` varchar(20) DEFAULT NULL,
  `reason2` varchar(20) DEFAULT NULL,
  `employer3` varchar(55) DEFAULT NULL,
  `post3` varchar(30) DEFAULT NULL,
  `fromto3` varchar(20) DEFAULT NULL,
  `reason3` varchar(20) DEFAULT NULL,
  `employer4` varchar(55) DEFAULT NULL,
  `post4` varchar(30) DEFAULT NULL,
  `fromto4` varchar(20) DEFAULT NULL,
  `reason4` varchar(20) DEFAULT NULL,
  `employer5` varchar(55) DEFAULT NULL,
  `post5` varchar(30) DEFAULT NULL,
  `fromto5` varchar(20) DEFAULT NULL,
  `reason5` varchar(20) DEFAULT NULL,
  `employer6` varchar(55) DEFAULT NULL,
  `post6` varchar(30) DEFAULT NULL,
  `fromto6` varchar(20) DEFAULT NULL,
  `reason6` varchar(20) DEFAULT NULL,
  `relative1` varchar(55) DEFAULT NULL,
  `ageyob1` varchar(12) DEFAULT NULL,
  `relation1` varchar(12) DEFAULT NULL,
  `relative1pro` varchar(25) DEFAULT NULL,
  `relative2` varchar(55) DEFAULT NULL,
  `ageyob2` varchar(12) DEFAULT NULL,
  `relation2` varchar(12) DEFAULT NULL,
  `relative2pro` varchar(25) DEFAULT NULL,
  `relative3` varchar(55) DEFAULT NULL,
  `ageyob3` varchar(12) DEFAULT NULL,
  `relation3` varchar(12) DEFAULT NULL,
  `relative3pro` varchar(25) DEFAULT NULL,
  `relative4` varchar(55) DEFAULT NULL,
  `ageyob4` varchar(12) DEFAULT NULL,
  `relation4` varchar(12) DEFAULT NULL,
  `relative4pro` varchar(25) DEFAULT NULL,
  `relative5` varchar(55) DEFAULT NULL,
  `ageyob5` varchar(12) DEFAULT NULL,
  `relation5` varchar(12) DEFAULT NULL,
  `relative5pro` varchar(25) DEFAULT NULL,
  `relative6` varchar(55) DEFAULT NULL,
  `ageyob6` varchar(12) DEFAULT NULL,
  `relation6` varchar(12) DEFAULT NULL,
  `relative6pro` varchar(25) DEFAULT NULL,
  `relative7` varchar(55) DEFAULT NULL,
  `ageyob7` varchar(12) DEFAULT NULL,
  `relation7` varchar(12) DEFAULT NULL,
  `relative7pro` varchar(25) DEFAULT NULL,
  `relative8` varchar(55) DEFAULT NULL,
  `ageyob8` varchar(12) DEFAULT NULL,
  `relation8` varchar(12) DEFAULT NULL,
  `relative8pro` varchar(25) DEFAULT NULL,
  `relative9` varchar(55) DEFAULT NULL,
  `ageyob9` varchar(12) DEFAULT NULL,
  `relation9` varchar(12) DEFAULT NULL,
  `relative9pro` varchar(25) DEFAULT NULL,
  `esino` varchar(55) DEFAULT NULL,
  `esiempr` varchar(55) DEFAULT NULL,
  `localoffice` varchar(55) DEFAULT NULL,
  `esinomi` varchar(12) DEFAULT NULL,
  `esipartic` varchar(25) DEFAULT NULL,
  `esifamily` varchar(25) DEFAULT NULL,
  `pfacno` varchar(25) DEFAULT NULL,
  `pfnomes` varchar(25) DEFAULT NULL,
  `pfshares` varchar(25) DEFAULT NULL,
  `pfcpension` varchar(25) DEFAULT NULL,
  `pfwpension` varchar(25) DEFAULT NULL,
  `granomes` varchar(12) DEFAULT NULL,
  `grashares` varchar(25) DEFAULT NULL,
  `witness1` varchar(55) DEFAULT NULL,
  `witness1add` varchar(120) DEFAULT NULL,
  `witness2` varchar(55) DEFAULT NULL,
  `witness2add` varchar(120) DEFAULT NULL,
  `anyrelative` varchar(1) DEFAULT NULL,
  `relativename` varchar(55) DEFAULT NULL,
  `relationship` varchar(20) DEFAULT NULL,
  UNIQUE KEY `hr_emps_info_empid` (`empid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hr_emps_info`
--

LOCK TABLES `hr_emps_info` WRITE;
/*!40000 ALTER TABLE `hr_emps_info` DISABLE KEYS */;
INSERT INTO `hr_emps_info` VALUES (1,'INDIAN','H','AZEKEREK','PNIDKDK','LDCIEKEKE','PSDFDS',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `hr_emps_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-16 21:53:03
