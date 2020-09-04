-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Sep 04, 2020 at 06:51 AM
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
-- Table structure for table `Accounts`
--

CREATE TABLE `Accounts` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `fathersname` varchar(50) DEFAULT NULL,
  `mothersname` varchar(50) DEFAULT NULL,
  `age` int(10) DEFAULT NULL,
  `contact` varchar(40) DEFAULT NULL,
  `Account_id` varchar(100) DEFAULT NULL,
  `created_time` date DEFAULT NULL,
  `is_suspended` tinyint(1) DEFAULT 0,
  `location` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Accounts`
--

INSERT INTO `Accounts` (`id`, `user_id`, `first_name`, `last_name`, `fathersname`, `mothersname`, `age`, `contact`, `Account_id`, `created_time`, `is_suspended`, `location`) VALUES
(36, 26, 'Gaurav', 'Jha', 'Manoj Jha', 'Binita Jha', 18, '9819696573', 'e81c5d7c-17bf-4f09-bb67-9359a630071e', '2020-08-25', 0, 'KTM Nepal'),
(50, 28, 'Test First Name', 'Test Last Name', 'Test Fathers Name', 'Tests Mothers Name', 18, '98145369254', '11e389f4-a903-4de8-bf43-9d361d9d532d', '2020-08-26', 0, 'Kathmandu#Test');

-- --------------------------------------------------------

--
-- Table structure for table `Acc_to_check`
--

CREATE TABLE `Acc_to_check` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `First_Name` varchar(50) DEFAULT NULL,
  `Last_Name` varchar(50) DEFAULT NULL,
  `Fathers_Name` varchar(50) DEFAULT NULL,
  `Mothers_Name` varchar(50) DEFAULT NULL,
  `Age` int(20) DEFAULT NULL,
  `Citizenship_Number` varchar(50) DEFAULT NULL,
  `Location` varchar(50) DEFAULT NULL,
  `Contact` varchar(20) DEFAULT NULL,
  `Education` varchar(50) DEFAULT NULL,
  `Work` varchar(20) DEFAULT NULL,
  `is_seen` tinyint(1) DEFAULT 0,
  `is_rejectable` tinyint(1) DEFAULT 0,
  `Remarks` varchar(100) DEFAULT 'Sent to admin'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Acc_to_check`
--

INSERT INTO `Acc_to_check` (`id`, `user_id`, `First_Name`, `Last_Name`, `Fathers_Name`, `Mothers_Name`, `Age`, `Citizenship_Number`, `Location`, `Contact`, `Education`, `Work`, `is_seen`, `is_rejectable`, `Remarks`) VALUES
(10, 26, 'Gaurav', 'Jha', 'Manoj Jha', 'Binita Jha', 18, 'adsasjdasjhd', 'KTM Nepal', '98196573', 'Bachlores', 'Nope', 0, 1, 'Sent to admin'),
(12, 28, 'Test First Name', 'Test Last Name', 'Test Fathers Name', 'Tests Mothers Name', 18, '981-aasd-4512asd', 'Kathmandu#Test', '98145369254', 'SEE', 'Nope', 0, 1, 'Sent to admin'),
(13, 28, 'Test Firstname1', 'TestlastName1', 'Test Fathersname1', 'Test Mothersname1', 17, '85632126532-123asd', 'Test@Nepal', '98444556622', 'Computer Science', 'Test@Stude', 0, 0, 'Education is not speified correctly');

-- --------------------------------------------------------

--
-- Table structure for table `Balance`
--

CREATE TABLE `Balance` (
  `id` int(11) NOT NULL,
  `acc_id` int(11) DEFAULT NULL,
  `Credit_Amount` int(150) DEFAULT NULL,
  `Debit_Amount` int(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Balance`
--

INSERT INTO `Balance` (`id`, `acc_id`, `Credit_Amount`, `Debit_Amount`) VALUES
(24, 36, 1000, 500),
(26, 50, 500, 484);

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
(8, 26, 1, 'Dog'),
(9, 28, 2, 'MTPS'),
(10, 29, 1, 'Blacky');

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
  `contact` varchar(255) DEFAULT NULL,
  `faculty` enum('admin','staff','user','manager') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id`, `first_name`, `last_name`, `age`, `username`, `password`, `address`, `contact`, `faculty`) VALUES
(26, 'Gaurav', 'Jha', 18, 'Pyderator', 'Highway', 'KTM', '9819696573', 'admin'),
(28, 'Test', 'Ing', 20, 'Test', 'test1', 'Kathmandu', '9819696573', NULL),
(29, 'Test1', 'Test2', 12, 'Testing1', 'Testing123', 'Test@Nepal', '9866622222', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Accounts`
--
ALTER TABLE `Accounts`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Account_id` (`Account_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `Acc_to_check`
--
ALTER TABLE `Acc_to_check`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `Balance`
--
ALTER TABLE `Balance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `acc_id` (`acc_id`);

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
-- AUTO_INCREMENT for table `Accounts`
--
ALTER TABLE `Accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `Acc_to_check`
--
ALTER TABLE `Acc_to_check`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `Balance`
--
ALTER TABLE `Balance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `Questions`
--
ALTER TABLE `Questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Accounts`
--
ALTER TABLE `Accounts`
  ADD CONSTRAINT `Accounts_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

--
-- Constraints for table `Acc_to_check`
--
ALTER TABLE `Acc_to_check`
  ADD CONSTRAINT `Acc_to_check_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

--
-- Constraints for table `Balance`
--
ALTER TABLE `Balance`
  ADD CONSTRAINT `Balance_ibfk_1` FOREIGN KEY (`acc_id`) REFERENCES `Accounts` (`id`);

--
-- Constraints for table `Questions`
--
ALTER TABLE `Questions`
  ADD CONSTRAINT `Questions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
