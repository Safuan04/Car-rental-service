-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: carrent_db
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car` (
  `id` int NOT NULL AUTO_INCREMENT,
  `make` varchar(128) DEFAULT NULL,
  `model` varchar(128) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `Seating` int DEFAULT NULL,
  `description` text,
  `daily_price` float DEFAULT NULL,
  `availability` tinyint(1) DEFAULT NULL,
  `date_posted` datetime NOT NULL,
  `img_file` varchar(256) DEFAULT NULL,
  `owner_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `car_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `owner` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (1,'FORD','Explorer Sport',2013,7,'2013 Ford Explorer Sport: Power meets versatility. Turbocharged V6, all-wheel drive, and room for seven. A blend of performance and comfort in one SUV.',400,NULL,'2023-12-02 20:52:45','dcc4463c9f78846c.jpeg',1),(2,'SEAT','Leon',2017,5,'A sleek, sporty compact with a stylish design and dynamic performance, blending comfort with modern tech.',200,NULL,'2023-12-02 21:03:39','2436e9e80aa99671.jpg',2),(3,'BMW','e92',2014,4,'BMW E92: Unleash thrill and luxury. Iconic design, precision performance, and the epitome of driving pleasure.',250,NULL,'2023-12-02 21:16:41','3fe79532cb3d3b87.jpg',1),(4,'DACIA','Duster',2015,5,'an exceptional SUV that combines affordability with reliability. With its budget-friendly rates and dependable performance, the Dacia Duster ensures a comfortable and enjoyable ride for your journey ahead.',400,NULL,'2023-12-02 21:36:15','135272292313ec86.jpg',3),(5,'DACIA','Sandero',2017,5,'Experience simplicity and value in this budget-friendly ride! The Dacia Sandero of 2017 is your ticket to hassle-free travels. With its spacious interiors and efficient performance, this car is perfect for your daily commute or weekend getaways',250,NULL,'2023-12-02 21:40:28','d51a6ba5960aad17.jpg',3),(6,'TOYOTA','Corolla',2021,5,'The Toyota Corolla has been a long-standing favorite in the automotive world, renowned for its reliability, fuel efficiency, and practicality.',350,NULL,'2023-12-02 21:42:07','107f04718ef0a9f1.jpg',1);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `owner`
--

DROP TABLE IF EXISTS `owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `owner` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `address` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owner`
--

LOCK TABLES `owner` WRITE;
/*!40000 ALTER TABLE `owner` DISABLE KEYS */;
INSERT INTO `owner` VALUES (1,'SafuanCars','AV OTHMAN BEN AFFAN ZKT 36'),(2,'AdilCars','AV FAR 344'),(3,'MaruanCars','AV TANGER KZENAYA 224'),(4,'HaitamCars','AV TOUIBLA OUED TANSIFT');
/*!40000 ALTER TABLE `owner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `car_id` int NOT NULL,
  `user_id` int NOT NULL,
  `owner_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `car_id` (`car_id`),
  KEY `user_id` (`user_id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`car_id`) REFERENCES `car` (`id`),
  CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `reservation_ibfk_3` FOREIGN KEY (`owner_id`) REFERENCES `owner` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (1,'2023-12-03','2023-12-04',3,1,1);
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `img_file` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Safuan','safuan@demo.com','$2b$12$fanA06pZaOZk8VSHi47u7ujv.heSR.EVJMruNj3ppah.RcHERGT26','default.jpg'),(2,'Haytam','haytam@demo.com','$2b$12$/tWWwAm543bVmtfywhvq/ecbyrfzBKLnmVKuZLXCa9b4ZMtDYv3za','default.jpg');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-04 19:57:18
