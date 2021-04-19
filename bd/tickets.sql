-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-04-2021 a las 03:13:16
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tickets`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tickets`
--

CREATE TABLE `tickets` (
  `ticket` int(11) NOT NULL,
  `dateStart` datetime NOT NULL,
  `subject` varchar(500) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `employee` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `dateEnd` datetime DEFAULT NULL,
  `employeeEnvia` varchar(100) DEFAULT NULL,
  `employeeResibe` varchar(100) DEFAULT NULL,
  `note` text DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tickets`
--

INSERT INTO `tickets` (`ticket`, `dateStart`, `subject`, `status`, `employee`, `description`, `dateEnd`, `employeeEnvia`, `employeeResibe`, `note`, `email`, `password`) VALUES
(13, '2020-04-29 00:00:00', 'todo funciona bien', 1, 'Angel Rodriguezetp', 'tochido carnal', NULL, NULL, NULL, NULL, '', ''),
(15, '2021-04-21 09:34:00', 'good job', 2, 'faw', 'listo', '2021-04-24 10:33:21', 'lisset', 'manuel', 'gracias por la solu=y=uccion', '', ''),
(17, '2021-04-20 10:23:00', '', 0, '', '', '2021-04-21 00:24:00', NULL, NULL, NULL, '', ''),
(23, '0000-00-00 00:00:00', '', 0, '', '', NULL, NULL, NULL, NULL, '20187068@itla.edu.do', '1230'),
(24, '0000-00-00 00:00:00', '', 0, '', '', NULL, NULL, NULL, NULL, 'drodriguez21031@gmail.com', '1456'),
(25, '0000-00-00 00:00:00', '', 0, '', '', NULL, NULL, NULL, NULL, '20187068@itla.edu.do', '1020');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tickets`
--
ALTER TABLE `tickets`
  ADD PRIMARY KEY (`ticket`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tickets`
--
ALTER TABLE `tickets`
  MODIFY `ticket` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
