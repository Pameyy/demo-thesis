-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 20, 2020 at 02:38 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `id` int(10) NOT NULL,
  `month` int(10) NOT NULL,
  `year` int(10) NOT NULL,
  `date` date NOT NULL,
  `water` int(10) NOT NULL,
  `electric` int(10) NOT NULL,
  `cost_total` int(10) NOT NULL,
  `room_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`id`, `month`, `year`, `date`, `water`, `electric`, `cost_total`, `room_id`) VALUES
(113, 4, 2563, '2020-04-28', 16, 348, 2864, 1),
(114, 4, 2563, '2020-04-28', 0, 54, 2554, 2),
(115, 4, 2563, '2020-04-28', 0, 96, 2596, 3),
(116, 4, 2563, '2020-04-28', 16, 324, 2840, 4),
(117, 4, 2563, '2020-04-28', 0, 174, 2674, 5),
(119, 5, 2563, '2020-05-30', 0, 126, 2626, 1),
(120, 5, 2563, '2020-05-30', 0, 42, 2542, 2),
(121, 5, 2563, '2020-05-30', 0, 36, 2536, 3),
(122, 5, 2563, '2020-05-30', 40, 1344, 3884, 4),
(123, 5, 2563, '2020-05-30', 0, 90, 2590, 5),
(125, 6, 2563, '2020-06-29', 8, 234, 2742, 1),
(126, 6, 2563, '2020-06-29', 0, 36, 2536, 2),
(127, 6, 2563, '2020-06-29', 0, 6, 2506, 3),
(128, 6, 2563, '2020-06-29', 40, 990, 3530, 4),
(129, 6, 2563, '2020-06-29', 24, 1038, 3562, 5),
(131, 7, 2563, '2020-07-29', 32, 462, 2994, 1),
(132, 7, 2563, '2020-07-29', 8, 48, 2556, 2),
(133, 7, 2563, '2020-07-29', 0, 0, 2500, 3),
(134, 7, 2563, '2020-07-29', 8, 150, 2658, 4),
(135, 7, 2563, '2020-07-29', 16, 654, 3170, 5),
(137, 8, 2563, '2020-08-29', 24, 336, 2860, 1),
(138, 8, 2563, '2020-08-29', 16, 144, 2660, 2),
(139, 8, 2563, '2020-08-29', 0, 0, 2500, 3),
(140, 8, 2563, '2020-08-29', 8, 318, 2826, 4),
(141, 8, 2563, '2020-08-29', 16, 564, 3080, 5),
(143, 9, 2563, '2020-10-05', 24, 462, 2986, 1),
(144, 9, 2563, '2020-10-06', 24, 462, 2986, 1),
(145, 5, 2563, '2020-10-06', 0, 126, 2626, 1),
(146, 5, 2563, '2020-10-06', 0, 126, 2626, 1),
(147, 5, 2563, '2020-10-06', 0, 126, 2626, 1),
(148, 8, 2563, '2020-10-06', 24, 336, 2860, 1),
(149, 8, 2563, '2020-10-06', 24, 336, 2860, 1),
(150, 6, 2563, '2020-10-07', 8, 234, 2742, 1),
(151, 8, 2563, '2020-10-07', 24, 336, 2860, 1),
(152, 5, 2563, '2020-10-07', 40, 1344, 3884, 4),
(153, 7, 2563, '2020-10-08', 8, 150, 2658, 4),
(154, 7, 2563, '2020-10-08', 0, 0, 2500, 3),
(155, 5, 2563, '2020-10-09', 0, 36, 2536, 3),
(156, 5, 2563, '2020-10-09', 0, 126, 2626, 1),
(157, 5, 2563, '2020-10-09', 0, 126, 2626, 1),
(158, 5, 2563, '2020-10-09', 0, 36, 2536, 3),
(159, 6, 2563, '2020-10-09', 0, 36, 2536, 2),
(160, 6, 2563, '2020-10-09', 0, 36, 2536, 2),
(161, 6, 2563, '2020-10-09', 0, 36, 2536, 2),
(162, 6, 2563, '2020-10-09', 0, 6, 2506, 3),
(163, 7, 2563, '2020-10-09', 16, 654, 3170, 5),
(164, 6, 2563, '2020-10-10', 40, 990, 3530, 4),
(165, 4, 2563, '2020-10-11', 16, 348, 2864, 1),
(168, 8, 2563, '2020-10-13', 24, 336, 2860, 1),
(169, 7, 2563, '2020-10-26', 32, 462, 2994, 1),
(170, 8, 2563, '2020-10-26', 8, 318, 2826, 4),
(171, 4, 2563, '2020-10-26', 16, 348, 2864, 1),
(172, 9, 2563, '2020-10-27', 5896, 58812, 67208, 3),
(173, 9, 2563, '2020-10-28', 6672, 55374, 64546, 2),
(174, 7, 2563, '2020-10-29', 32, 462, 2994, 1),
(175, 9, 2563, '2020-10-30', 7184, 39432, 49116, 5),
(176, 8, 2563, '2020-10-30', 24, 336, 2860, 1),
(177, 9, 2563, '2020-10-31', 6672, 55374, 64546, 2);

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `month` int(10) NOT NULL,
  `year` int(10) NOT NULL,
  `date` date NOT NULL,
  `water` int(10) NOT NULL,
  `electric` int(10) NOT NULL,
  `cost_total` int(10) NOT NULL,
  `before_meter` int(10) NOT NULL,
  `before_water` int(10) NOT NULL,
  `after_meter` int(10) NOT NULL,
  `after_water` int(10) NOT NULL,
  `room_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id`, `month`, `year`, `date`, `water`, `electric`, `cost_total`, `before_meter`, `before_water`, `after_meter`, `after_water`, `room_id`) VALUES
(1, 8, 2563, '2020-10-06', 24, 336, 2860, 8367, 454, 8423, 457, 1),
(2, 6, 2563, '2020-10-07', 8, 234, 2742, 8251, 449, 8290, 450, 1),
(3, 8, 2563, '2020-10-07', 24, 336, 2860, 8367, 454, 8423, 457, 1),
(4, 5, 2563, '2020-10-07', 40, 1344, 3884, 5885, 451, 6109, 456, 4),
(5, 7, 2563, '2020-10-08', 8, 150, 2658, 6274, 461, 6299, 462, 4),
(6, 7, 2563, '2020-10-08', 0, 0, 2500, 7753, 479, 7753, 479, 3),
(7, 6, 2563, '2020-10-09', 0, 36, 2536, 9449, 379, 9455, 379, 2),
(8, 6, 2563, '2020-10-09', 0, 36, 2536, 9449, 379, 9455, 379, 2),
(9, 6, 2563, '2020-10-09', 0, 36, 2536, 9449, 379, 9455, 379, 2),
(10, 6, 2563, '2020-10-09', 0, 6, 2506, 7752, 479, 7753, 479, 3),
(11, 7, 2563, '2020-10-09', 16, 654, 3170, 780, 314, 889, 316, 5),
(12, 6, 2563, '2020-10-10', 40, 990, 3530, 6109, 456, 6274, 461, 4),
(13, 4, 2563, '2020-10-11', 16, 348, 2864, 8172, 447, 8230, 449, 1),
(14, 7, 2563, '2020-10-13', 0, 0, 2500, 7753, 479, 7753, 479, 3),
(15, 9, 2563, '2020-10-13', 7424, 48336, 58260, 8423, 457, 6479, 385, 1),
(16, 8, 2563, '2020-10-13', 24, 336, 2860, 8367, 454, 8423, 457, 1),
(17, 7, 2563, '2020-10-26', 32, 462, 2994, 8290, 450, 8367, 454, 1),
(18, 8, 2563, '2020-10-26', 8, 318, 2826, 6299, 462, 6352, 463, 4),
(19, 4, 2563, '2020-10-26', 16, 348, 2864, 8172, 447, 8230, 449, 1),
(20, 9, 2563, '2020-10-27', 5896, 58812, 67208, 7753, 479, 7555, 216, 3),
(21, 9, 2563, '2020-10-28', 6672, 55374, 64546, 9487, 382, 8716, 216, 2),
(22, 7, 2563, '2020-10-29', 32, 462, 2994, 8290, 450, 8367, 454, 1),
(23, 9, 2563, '2020-10-30', 7184, 39432, 49116, 983, 318, 7555, 216, 5),
(24, 8, 2563, '2020-10-30', 24, 336, 2860, 8367, 454, 8423, 457, 1),
(25, 9, 2563, '2020-10-31', 6672, 55374, 64546, 9487, 382, 8716, 216, 2);

-- --------------------------------------------------------

--
-- Table structure for table `image_path`
--

CREATE TABLE `image_path` (
  `id` int(11) NOT NULL,
  `month` int(10) NOT NULL,
  `year` int(10) NOT NULL,
  `path_meter` varchar(255) NOT NULL,
  `path_water` varchar(255) NOT NULL,
  `room_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `image_path`
--

INSERT INTO `image_path` (`id`, `month`, `year`, `path_meter`, `path_water`, `room_id`) VALUES
(1, 9, 2563, 'static/upload/meter\\23.jpg', 'static/upload/water\\23.jpg', 1),
(2, 7, 2563, 'static/upload/meter\\36.jpg', 'static/upload/water\\36.jpg', 3),
(3, 8, 2563, 'static/upload/meter\\37.jpg', 'static/upload/water\\37.jpg', 2),
(4, 6, 2563, 'static/upload/meter\\39.jpg', 'static/upload/water\\39.jpg', 4),
(5, 9, 2563, 'static/upload/meter\\44.jpg', 'static/upload/water\\44.jpg', 9),
(6, 9, 2563, 'static/upload/meter\\45.jpg', 'static/upload/water\\45.jpg', 1),
(7, 9, 2563, 'static/upload/meter\\46.jpg', 'static/upload/water\\46.jpg', 4),
(8, 10, 2563, 'static/upload/meter\\82.jpg', 'static/upload/water\\82.jpg', 1),
(9, 9, 2563, 'static/upload/meter\\83.jpg', 'static/upload/water\\83.jpg', 3),
(10, 9, 2563, 'static/upload/meter\\85.jpg', 'static/upload/water\\85.jpg', 2),
(11, 9, 2563, 'static/upload/meter\\86.jpg', 'static/upload/water\\86.jpg', 9),
(12, 9, 2563, 'static/upload/meter\\87.jpg', 'static/upload/water\\87.jpg', 5),
(13, 8, 2563, 'static/upload/meter\\88.jpg', 'static/upload/water\\88.jpg', 1),
(14, 6, 2563, 'static/upload/meter\\90.jpg', 'static/upload/water\\90.jpg', 2);

-- --------------------------------------------------------

--
-- Table structure for table `meter`
--

CREATE TABLE `meter` (
  `id` int(10) NOT NULL,
  `month` int(10) NOT NULL,
  `year` int(10) NOT NULL,
  `number_electric` int(10) NOT NULL,
  `number_water` int(10) NOT NULL,
  `room_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `meter`
--

INSERT INTO `meter` (`id`, `month`, `year`, `number_electric`, `number_water`, `room_id`) VALUES
(14, 3, 2563, 8172, 447, 1),
(15, 3, 2563, 9433, 379, 2),
(16, 3, 2563, 7730, 479, 3),
(17, 3, 2563, 5831, 449, 4),
(18, 3, 2563, 563, 311, 5),
(20, 4, 2563, 8230, 449, 1),
(21, 4, 2563, 9442, 379, 2),
(22, 4, 2563, 7746, 479, 3),
(23, 4, 2563, 5885, 451, 4),
(24, 4, 2563, 592, 311, 5),
(26, 5, 2563, 8251, 449, 1),
(27, 5, 2563, 9449, 379, 2),
(28, 5, 2563, 7752, 479, 3),
(29, 5, 2563, 6109, 456, 4),
(30, 5, 2563, 607, 311, 5),
(32, 6, 2563, 8290, 450, 1),
(33, 6, 2563, 9455, 379, 2),
(34, 6, 2563, 7753, 479, 3),
(35, 6, 2563, 6274, 461, 4),
(36, 6, 2563, 780, 314, 5),
(38, 7, 2563, 8367, 454, 1),
(39, 7, 2563, 9463, 380, 2),
(40, 7, 2563, 7753, 479, 3),
(41, 7, 2563, 6299, 462, 4),
(42, 7, 2563, 889, 316, 5),
(44, 8, 2563, 8423, 457, 1),
(45, 8, 2563, 9487, 382, 2),
(46, 8, 2563, 7753, 479, 3),
(47, 8, 2563, 6352, 463, 4),
(48, 8, 2563, 983, 318, 5),
(76, 9, 2563, 8290, 746, 4),
(77, 10, 2563, 7555, 216, 1),
(78, 9, 2563, 7555, 216, 3),
(79, 9, 2563, 8716, 216, 2),
(80, 9, 2563, 7555, 216, 9),
(81, 9, 2563, 7555, 216, 5),
(82, 8, 2563, 8716, 216, 1),
(83, 6, 2563, 7555, 8699, 2);

-- --------------------------------------------------------

--
-- Table structure for table `month`
--

CREATE TABLE `month` (
  `id_month` int(10) NOT NULL,
  `month` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `month`
--

INSERT INTO `month` (`id_month`, `month`) VALUES
(1, 'มกราคม'),
(2, 'กุมภาพันธ์'),
(3, ' มีนาคม'),
(4, ' เมษายน'),
(5, 'พฤษภาคม'),
(6, 'มิถุนายน'),
(7, 'กรกฎาคม'),
(8, 'สิงหาคม'),
(9, 'กันยายน'),
(10, 'ตุลาคม'),
(11, 'พฤศจิกายน'),
(12, 'ธันวาคม');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `id` int(10) NOT NULL,
  `room_name` varchar(50) NOT NULL,
  `user_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`id`, `room_name`, `user_id`) VALUES
(1, 'B-1', 1),
(2, 'B-2', 4),
(3, 'C-1', 5),
(4, 'C-2', 6),
(5, 'D-1', 7),
(9, 'D-2', 16);

-- --------------------------------------------------------

--
-- Table structure for table `units`
--

CREATE TABLE `units` (
  `id` int(10) NOT NULL,
  `unit_meter` int(10) NOT NULL,
  `unit_water` int(10) NOT NULL,
  `rent_room` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `units`
--

INSERT INTO `units` (`id`, `unit_meter`, `unit_water`, `rent_room`) VALUES
(1, 6, 8, 2500);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fullname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `tel` varchar(10) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `fullname`, `email`, `tel`, `status`) VALUES
(1, 'B-1', 'roomb-1', 'B-1', 'b-1@gmail.com', '0931317505', 'resident'),
(2, 'admin', 'password', 'admin', 'admin@g.com', '', 'staff'),
(3, 'owner', 'password', 'owner', 'owner@g.com', '', 'staff'),
(4, 'B-2', 'roomb-2', 'B-2', 'b-2@g.com', '', 'resident'),
(5, 'C-1', 'roomc-1', 'C-1', 'c-1@g.com', '', 'resident'),
(6, 'C-2', 'roomc-2', 'C-2', 'C-2@g.com', '1234566789', 'staff'),
(7, 'D-1', 'roomd-1', 'D-1', 'D-1@g.com', '', 'resident'),
(16, 'D-2', 'roomd-2', 'D-2', 'd-2@gmail.com', '123456789', 'resident');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_id` (`room_id`),
  ADD KEY `month` (`month`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_id` (`room_id`),
  ADD KEY `month` (`month`);

--
-- Indexes for table `image_path`
--
ALTER TABLE `image_path`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_id` (`room_id`);

--
-- Indexes for table `meter`
--
ALTER TABLE `meter`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_id` (`room_id`);

--
-- Indexes for table `month`
--
ALTER TABLE `month`
  ADD PRIMARY KEY (`id_month`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `units`
--
ALTER TABLE `units`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bill`
--
ALTER TABLE `bill`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=178;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `image_path`
--
ALTER TABLE `image_path`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `meter`
--
ALTER TABLE `meter`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT for table `month`
--
ALTER TABLE `month`
  MODIFY `id_month` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `room`
--
ALTER TABLE `room`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `units`
--
ALTER TABLE `units`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`month`) REFERENCES `month` (`id_month`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `history`
--
ALTER TABLE `history`
  ADD CONSTRAINT `history_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `history_ibfk_2` FOREIGN KEY (`month`) REFERENCES `month` (`id_month`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `image_path`
--
ALTER TABLE `image_path`
  ADD CONSTRAINT `image_path_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `meter`
--
ALTER TABLE `meter`
  ADD CONSTRAINT `meter_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `room_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
