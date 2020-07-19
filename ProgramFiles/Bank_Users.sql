-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jul 19, 2020 at 06:29 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Bank_Users`
--

-- --------------------------------------------------------

--
-- Table structure for table `Questions`
--

CREATE TABLE `Questions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `Question_id` int(20) DEFAULT NULL,
  `answer` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Questions`
--

INSERT INTO `Questions` (`id`, `user_id`, `Question_id`, `answer`) VALUES
(1, 20, 2, 'MTPS'),
(2, 21, 1, 'Blacky');

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `address` varchar(40) DEFAULT NULL,
  `contact` int(20) DEFAULT NULL,
  `faculty` enum('admin','staff','user','manager') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id`, `first_name`, `last_name`, `age`, `username`, `password`, `address`, `contact`, `faculty`) VALUES
(1, 'Gaurav', 'Jha ', 20, 'Pyderator', 'test', 'KTM,Nepal', 98100, NULL),
(4, '5', '5', 5, '5', '5', '5', 5, NULL),
(5, '5', '5', 5, '5', '5', '5', 5, NULL),
(6, '4', '4', 4, '4', '4', '4', 4, NULL),
(7, '3', '3', 3, '3', '33', '33', 3, NULL),
(8, '3', '3', 3, '3', '3', '33', 3, NULL),
(9, 'a', 'b', 2, 'b', 'b', 'b', 2, NULL),
(10, '8', '8', 8, '8', '8', '8', 8, NULL),
(11, '324', '4865', 56412, '564', '56', '312', 45612, NULL),
(13, '41ad', '5421', 741, '541', '541', '75412', 74518, NULL),
(14, '7', '7', 7, '7', '7', '7', 7, NULL),
(15, '9', '9', 99, '9', '9', '9', 9, NULL),
(16, '7', '7', 7, '7', '7', '7', 7, NULL),
(17, 'test1', '11', 11, '111', '111', '111', 111, NULL),
(18, '89', '98', 98, '98', '98', '98', 8998, NULL),
(19, '78', '87', 87, '87', '87', '87', 87, NULL),
(20, 'GGAARR', 'JJHHAA', 5, 'oscar', 'mike', 'ktm', 65, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Questions`
--
ALTER TABLE `Questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Questions`
--
ALTER TABLE `Questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Questions`
--
ALTER TABLE `Questions`
  ADD CONSTRAINT `Questions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
