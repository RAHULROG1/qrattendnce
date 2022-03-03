/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - py_attendence_qr
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`py_attendence_qr` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `py_attendence_qr`;

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `period_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`student_id`,`period_id`,`date`) values (1,1,1,'2022-10-22'),(2,2,1,'2022-10-23'),(3,6,3,'2022-01-14'),(4,6,3,'2022-01-14'),(5,6,1,'2022-01-14'),(6,3,1,'2022-02-16'),(7,6,3,'2022-02-16'),(8,6,3,'2022-02-16');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(9,'aa','aa','teacher'),(11,'bb','bb','student'),(12,'cc','cc','student'),(13,'dd','dd','student');

/*Table structure for table `periods` */

DROP TABLE IF EXISTS `periods`;

CREATE TABLE `periods` (
  `period_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `fromtime` varchar(100) DEFAULT NULL,
  `totime` varchar(100) DEFAULT NULL,
  `qrcode` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`period_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `periods` */

insert  into `periods`(`period_id`,`subject`,`date`,`fromtime`,`totime`,`qrcode`) values (1,'Maths','2022-01-14','8:30','9',NULL),(3,'english','2022-02-17','9','9:30',NULL),(4,'newss','2022-02-15','12:00','12:30','static/qrcode/944381e0-f39d-4045-8a63-a67dd69df432.png');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

/*Data for the table `student` */

insert  into `student`(`student_id`,`login_id`,`firstname`,`lastname`,`place`,`age`,`email`) values (1,90,'ann','jose','kollam','27','ann@gmail.com'),(2,5,'jo','kr','dfgh','55','ghj'),(4,11,'Ben','k','kozhikode','22','ben@gmail.com'),(5,12,'mani','k','kollam','22','mani@gmail.com'),(6,13,'ani','l','kozhikode','27','sheril@gmail.com');

/*Table structure for table `teacher` */

DROP TABLE IF EXISTS `teacher`;

CREATE TABLE `teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `desgination` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `teacher` */

insert  into `teacher`(`teacher_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`,`desgination`) values (1,9,'Athira','l','kochi','9977664433','athira@gmail.com','proffessor');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
