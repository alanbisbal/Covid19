-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-11-2020 a las 20:55:30
-- Versión del servidor: 10.4.14-MariaDB
-- Versión de PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grupo37`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `centros`
--

CREATE TABLE `centros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `telefono` varchar(255) NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_fin` time NOT NULL,
  `municipio_id` varchar(255) NOT NULL,
  `web` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `estado_id` int(11) NOT NULL,
  `protocolo` varchar(255) DEFAULT NULL,
  `latitud` float NOT NULL,
  `longitud` float NOT NULL,
  `tipo_centro` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `centros`
--

INSERT INTO `centros` (`id`, `nombre`, `direccion`, `telefono`, `hora_inicio`, `hora_fin`, `municipio_id`, `web`, `email`, `estado_id`, `protocolo`, `latitud`, `longitud`, `tipo_centro`) VALUES
(19, 'Centro_publicado', 'calle 120 y 50', '123123', '08:00:00', '21:00:00', '19', 'info.unlp.com', 'info@unlp.com', 1, '07aef9c7-237d-11eb-8a2d-107b44b7ee2c.pdf', -57.9811, -34.9311, 3),
(20, 'Centro_despublicado', '120 y 500', '123123', '08:00:00', '22:00:00', '1', 'despub.com', 'despub@licado', 2, '07aef9c7-237d-11eb-8a2d-107b44b7ee2c.pdf', -57.9924, -34.9159, 2),
(21, 'Centro_pendiente', '50 y 21', '123123', '06:00:00', '18:00:00', '20', 'Centro_pendiente', 'Centro_pendiente@centro', 3, '07aef9c7-237d-11eb-8a2d-107b44b7ee2c.pdf', -57.9924, -34.9159, 4),
(22, 'asdasd', '123123', '213123', '17:06:00', '17:06:00', '9', 'asd', 'asd@asd', 3, 'dfedc882-2b6b-11eb-a4b8-107b44b7ee2c.pdf', -57.9924, -34.9159, 3),
(31, 'centroAyudaMuestra', 'centroAyudaMuestra', '123123', '08:00:00', '19:00:00', '19', 'centroAyudaMuestra', 'centroAyudaMuestra@gmail.com', 1, 'ab351d3f-2dba-11eb-9ea2-107b44b7ee2c.pdf', -56.9924, -32.9159, 3),
(45, 'Iglesia Sagrado Corazón de Jesús', 'Diagonal 73 nro 1032', '221 - 5139019', '09:30:00', '18:00:00', '24', '', 'asdasd@asdasd.com', 3, NULL, -57.9924, -34.9159, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `configs`
--

CREATE TABLE `configs` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `elementos` int(11) NOT NULL,
  `estado` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `configs`
--

INSERT INTO `configs` (`id`, `titulo`, `descripcion`, `email`, `elementos`, `estado`) VALUES
(1, 'Donaciones Covid19', 'En el contexto de pandemia por el cual atravesamos los mas vulnerables son los mas perjudicadosSolicita tu turno para donar ropa ,plasma y sangre en tu centro más cercano.También podes recibir donaciones en caso de necesitarlo', 'Covid19@donaciones.com', 40, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estados`
--

CREATE TABLE `estados` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estados`
--

INSERT INTO `estados` (`id`, `nombre`) VALUES
(1, 'Publicado'),
(2, 'Despublicado'),
(3, 'Pendiente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `permisos`
--

INSERT INTO `permisos` (`id`, `name`, `description`) VALUES
(1, 'user_index', 'permite acceder al index (listado) del módulo'),
(2, 'user_new', ' permite cargar un usuario'),
(3, 'user_destroy', 'permite borrar un usuario'),
(4, 'user_update', 'permite actualizar un usuario.\r\n'),
(5, 'user_show', 'permite visualizar un usuario'),
(7, 'centro_index', 'permite acceder al index (listado) del módulo'),
(9, 'centro_new', ' permite cargar un centro de ayuda social.'),
(11, 'centro_destroy', ' permite borrar un centro de ayuda social.\r\n'),
(13, 'centro_update', 'permite actualizar un centro de ayuda social'),
(15, 'centro_show', 'permite visualizar un centro de ayuda social'),
(16, 'permisos_index', ' permite acceder al index (listado) del módulo.'),
(17, 'user_perfil', 'permite al usuario visualizar su perfil'),
(18, 'permiso_admin', 'permite al usuario asignarle el permiso administrador'),
(19, 'turno_index', ' permite acceder al index (listado) del módulo de turnos'),
(20, 'turno_new', 'permite cargar un turno'),
(21, 'turno_destroy', 'permite borrar un turno'),
(22, 'turno_update', 'permite actualizar un turno'),
(23, 'turno_show', 'permite visualizar un turno');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rols`
--

CREATE TABLE `rols` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rols`
--

INSERT INTO `rols` (`id`, `name`, `description`) VALUES
(1, 'Administrador\r\n', 'Administrador general'),
(2, 'Operador', 'Administrador de centros');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rols_permisos`
--

CREATE TABLE `rols_permisos` (
  `id` int(11) NOT NULL,
  `rol_id` int(11) DEFAULT NULL,
  `permiso_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rols_permisos`
--

INSERT INTO `rols_permisos` (`id`, `rol_id`, `permiso_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(9, 1, 7),
(10, 1, 9),
(11, 1, 11),
(12, 1, 13),
(13, 1, 15),
(14, 1, 16),
(15, 1, 17),
(16, 2, 17),
(17, 1, 18),
(18, 2, 9),
(19, 2, 13),
(20, 2, 15),
(21, 2, 7),
(22, 1, 19),
(23, 2, 19),
(24, 1, 20),
(25, 1, 21),
(26, 1, 22),
(27, 1, 23),
(28, 2, 20),
(29, 2, 21),
(30, 2, 22),
(31, 2, 23),
(32, 2, 21),
(33, 2, 22),
(34, 2, 23),
(35, 2, 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_centros`
--

CREATE TABLE `tipo_centros` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_centros`
--

INSERT INTO `tipo_centros` (`id`, `nombre`) VALUES
(1, 'Institución religiosa'),
(2, 'Merendero'),
(3, 'Colegio '),
(4, 'Centro cultural');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefono` varchar(255) NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_fin` time NOT NULL,
  `fecha` date DEFAULT NULL,
  `centro_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`id`, `email`, `telefono`, `hora_inicio`, `hora_fin`, `fecha`, `centro_id`) VALUES
(13, 'admin', '123123', '09:00:00', '09:30:00', '2020-11-20', 19),
(15, 'asd', '123', '09:30:00', '10:00:00', '2020-11-20', 19),
(16, 'admin', '123123', '09:00:00', '09:30:00', '2020-11-21', 19),
(17, 'asd', '123', '09:00:00', '09:30:00', '2020-11-22', 19),
(18, 'asd', '', '09:30:00', '10:00:00', '2020-11-22', 19),
(19, 'asd', '', '10:00:00', '10:30:00', '2020-11-22', 19);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `activo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `first_name`, `last_name`, `password`, `activo`) VALUES
(1, 'Admin', 'admin@admin', 'Cosme', 'Fulanito', '123123', 1),
(2, 'Operador', 'operador@gmail.com', 'Lalo', 'Landa', '123123', 1),
(17, 'd', 'asdsad@dasd', 'a', 'd', 'asdasd', 1),
(18, 'eqweqwq', 'qweqwe@qweqwe', 'qweqwe', 'qweqweqw', 'qweqwe', 0),
(22, 'asd', 'asd@asd', 'asd', 'asd', 'asd', 1),
(25, 'qwerty', 'q@werty', 'qwerty', 'qwerty', '123123', 1),
(26, 'qwertya', 'q@wertya', 'qwertya', 'qwertya', '123123', 1),
(27, 'qwertyaasd', 'q@wertyaasd', 'qwertyaad', 'qwertyaasd', '123123', 1),
(28, 'qwertyaasdqwfqfw', 'q@wertyaasdfqwqwf', 'qwertyaadqewrwqar', 'qwertyaasdqwfqwf', '123123', 1),
(29, 'benitez', 'q@wertyaasdfqwqwfqwqw', 'qwertyaadqewrwqarewdq', 'qwertyaasdqwfqwfqwdwqd', '123123', 1),
(31, 'oooooooo', 'oooo@oo', 'ooooooo', 'ooooooooo', '123123', 1),
(32, 'oooooooooo', 'oooo@oooo', 'ooooooooo', 'ooooooooooo', '123123', 1),
(33, 'zzzzzzzzzzzzzzzzzz', 'zzz@zzz', 'zzzzzzzzz', 'zzzzzzzzzzzz', '123123', 1),
(34, 'zzzzzzzzzzzzzzzzzzaaaa', 'zzz@zzzaaa', 'zzzzzzzzz', 'zzzzzzzzzzzz', '123123', 1),
(35, 'zzzzzzzzzzzzzzzzzzaaaaaa', 'zzz@zzzaaaaa', 'zzzzzzzzz', 'zzzzzzzzzzzz', '123123', 1),
(36, 'rrrrrrrr', 'rrrr@rrrr', 'rrrrrr', 'rrrrrrr', '123123', 1),
(37, 'ccc', 'ccc@ccc', 'ccc', 'ccc', '123123', 1),
(38, 'yy', 'yy@yy', 'yy', 'yy', 'yyy', 1),
(39, 'yyy', 'yy@yyy', 'yyy', 'yyy', '123123', 1),
(40, 'con2', 'con2@rolespapu', 'alan', 'bisbal', '132123', 1),
(41, 'qwr3f', '12awfda@afhbua', 'adqdq', 'qwrwf', '123123', 1),
(43, 'asdasdasdasd', 'asdasda@asdsad', 'cosmeasdasd', 'asdasd', 'a123sad', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users_rols`
--

CREATE TABLE `users_rols` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `rol_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users_rols`
--

INSERT INTO `users_rols` (`id`, `user_id`, `rol_id`) VALUES
(1, 1, 1),
(10, 1, 2),
(11, 17, 2),
(12, 18, 2),
(15, 22, 2),
(17, 39, 1),
(18, 39, 2),
(19, 40, 1),
(20, 40, 2),
(21, 41, 2),
(24, 26, 1),
(31, 2, 1),
(32, 43, 1),
(33, 26, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `centros`
--
ALTER TABLE `centros`
  ADD PRIMARY KEY (`id`),
  ADD KEY `estado_id` (`estado_id`),
  ADD KEY `tipo_centro` (`tipo_centro`);

--
-- Indices de la tabla `configs`
--
ALTER TABLE `configs`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estados`
--
ALTER TABLE `estados`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rols`
--
ALTER TABLE `rols`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rols_permisos`
--
ALTER TABLE `rols_permisos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rol_id` (`rol_id`),
  ADD KEY `permiso_id` (`permiso_id`);

--
-- Indices de la tabla `tipo_centros`
--
ALTER TABLE `tipo_centros`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `centro_id` (`centro_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `users_rols`
--
ALTER TABLE `users_rols`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `rol_id` (`rol_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `centros`
--
ALTER TABLE `centros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `configs`
--
ALTER TABLE `configs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `estados`
--
ALTER TABLE `estados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `rols`
--
ALTER TABLE `rols`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `rols_permisos`
--
ALTER TABLE `rols_permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `tipo_centros`
--
ALTER TABLE `tipo_centros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT de la tabla `users_rols`
--
ALTER TABLE `users_rols`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `centros`
--
ALTER TABLE `centros`
  ADD CONSTRAINT `centros_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `estados` (`id`),
  ADD CONSTRAINT `centros_ibfk_2` FOREIGN KEY (`tipo_centro`) REFERENCES `tipo_centros` (`id`);

--
-- Filtros para la tabla `rols_permisos`
--
ALTER TABLE `rols_permisos`
  ADD CONSTRAINT `rols_permisos_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rols` (`id`),
  ADD CONSTRAINT `rols_permisos_ibfk_2` FOREIGN KEY (`permiso_id`) REFERENCES `permisos` (`id`);

--
-- Filtros para la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD CONSTRAINT `turnos_ibfk_1` FOREIGN KEY (`centro_id`) REFERENCES `centros` (`id`);

--
-- Filtros para la tabla `users_rols`
--
ALTER TABLE `users_rols`
  ADD CONSTRAINT `users_rols_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `users_rols_ibfk_2` FOREIGN KEY (`rol_id`) REFERENCES `rols` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
