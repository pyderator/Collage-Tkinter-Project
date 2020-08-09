-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 09, 2020 at 09:01 AM
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
(6, 22, 'Gaurav', 'Jha', 'Mr Manoj Jha', 'Binita Jha', 18, '9811100119', '28fcd38b-3ad1-439d-8805-d08324cb0719', '2020-07-25', 0, 'KTM'),
(7, 1, 'Gaurav', 'Jha', 'Manoj Jha', 'Binita Jha', 18, '9811100119', 'fd5a1a29-136b-4100-b8e8-409cd3b70146', '2020-07-25', 0, 'KTM'),
(8, 20, 'Gaurav', 'Jha', 'Mr Manoj Jha', 'Binita Jha', 18, '9811100119', 'da0fa88f-4100-4ec9-89c9-b5b023066d47', '2020-07-25', 0, 'KTM'),
(9, 1, 'Gaurav', 'Jha', 'Manoj Jha', 'Binita Jha', 18, '9811100119', '63fda5b7-fc52-48f8-8c93-75e6d210f5ed', '2020-07-25', 0, 'KTM'),
(18, 22, 'Gaurav', 'Jha', 'Mr Manoj Jha', 'Binita Jha', 18, '9811100119', '5cf32c52-7b77-4218-aa27-926d8e887c66', '2020-07-26', 0, 'KTM'),
(19, 20, 'Gaurav', 'Jha', 'Mr Manoj Jha', 'Binita Jha', 18, '9811100119', '1bf99bbb-eeb9-46e5-9897-5b8f017a7372', '2020-07-26', 0, 'KTM'),
(20, 20, 'Gaurav', 'Jha', 'Mr Manoj Jha', 'Binita Jha', 18, '9811100119', 'c3d53667-719c-4728-b363-cc12ab1d8f20', '2020-07-26', 0, 'KTM'),
(21, 20, 'Gaurav', 'Jha', 'Mr Manoj Jha', 'Binita Jha', 18, '9811100119', 'a3557d11-bd71-4353-8f95-b9baec521ed2', '2020-07-27', 0, 'KTM');

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
(1, 20, 'Gaurav1', 'Jha', 'Mr Manoj Jha', 'Binita Jha', 18, '0129312-2324-123123', 'KTM', '9811100119', 'BSC', 'No', 1, 0, 'Specify address!!!'),
(7, 1, 'Gaurav', 'Jha', 'Manoj Jha', 'Binita ', 18, '0129312-2324-123123', 'KTM, Nepal', '9811100119', 'IT', 'St', 0, 1, 'Address is not clear!!'),
(8, 22, 'asnd', 'nb', 'nb', 'nb', 52, 'asjcnxc90xmcn', 'mcnmsc', '241', 'axc', '', 0, 1, 'Sent to admin');

-- --------------------------------------------------------

--
-- Table structure for table `Balance`
--

CREATE TABLE `Balance` (
  `id` int(11) NOT NULL,
  `acc_id` int(11) DEFAULT NULL,
  `Credit_Amount` int(100) DEFAULT NULL,
  `Debit_Amount` int(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Balance`
--

INSERT INTO `Balance` (`id`, `acc_id`, `Credit_Amount`, `Debit_Amount`) VALUES
(1, 6, 130000, 5555),
(2, 18, 0, 13890),
(3, 20, 0, 0),
(4, 21, 0, 0);

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
(2, 21, 1, 'Blacky'),
(3, 22, 1, 'Dog');

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
(20, 'GGAARR', 'JJHHAA', 5, 'oscar', 'mike', 'ktm', 65, 'admin'),
(22, 'Gaurav', 'jha', 7, 'test', 'test', 'KTM', 798, NULL);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `Acc_to_check`
--
ALTER TABLE `Acc_to_check`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `Balance`
--
ALTER TABLE `Balance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `Questions`
--
ALTER TABLE `Questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

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
