INSERT INTO db_controlProyecto.proyecto_prioridad (prioridad)
VALUES ('Baja');

INSERT INTO db_controlProyecto.proyecto_prioridad (prioridad)
VALUES ('Media');

INSERT INTO db_controlProyecto.proyecto_prioridad (prioridad)
VALUES ('Alta');

INSERT INTO db_controlProyecto.proyecto_complejidad (complejidad)
VALUES ('Baja');

INSERT INTO db_controlProyecto.proyecto_complejidad (complejidad)
VALUES ('Media');

INSERT INTO db_controlProyecto.proyecto_complejidad (complejidad)
VALUES ('Alta');

INSERT INTO db_controlProyecto.proyecto_tiporequerimiento (tipoRequerimiento)
VALUES ('Requerimiento');

INSERT INTO db_controlProyecto.proyecto_tiporequerimiento (tipoRequerimiento)
VALUES ('Mejora');

INSERT INTO db_controlProyecto.proyecto_tiporequerimiento (tipoRequerimiento)
VALUES ('Bug');

INSERT INTO db_controlProyecto.proyecto_tiporequerimiento (tipoRequerimiento)
VALUES ('Otro');

INSERT INTO db_controlProyecto.proyecto_estadoproyecto (estadoProyecto)
VALUES ('Primer acercamiento');

INSERT INTO db_controlProyecto.proyecto_estadoproyecto (estadoProyecto)
VALUES ('Planificado');

INSERT INTO db_controlProyecto.proyecto_estadoproyecto (estadoProyecto)
VALUES ('En progreso');

INSERT INTO db_controlProyecto.proyecto_estadoproyecto (estadoProyecto)
VALUES ('En validacion');

INSERT INTO db_controlProyecto.proyecto_estadoproyecto (estadoProyecto)
VALUES ('Validado');

INSERT INTO db_controlProyecto.proyecto_estadoproyecto (estadoProyecto)
VALUES ('Desplegado');

INSERT INTO db_controlProyecto.proyecto_estadoproyecto (estadoProyecto)
VALUES ('Eliminado');

UPDATE `db_controlProyecto`.`proyecto_estadoproyecto` SET `idEstadoProyecto` = '99' WHERE (`idEstadoProyecto` = '7');

INSERT INTO `db_controlProyecto`.`requerimiento_estadorequerimiento` (`idEstadoRequerimiento`, `estadoRequerimiento`) VALUES ('1', 'Planificado');
INSERT INTO `db_controlProyecto`.`requerimiento_estadorequerimiento` (`idEstadoRequerimiento`, `estadoRequerimiento`) VALUES ('2', 'En progreso');
INSERT INTO `db_controlProyecto`.`requerimiento_estadorequerimiento` (`idEstadoRequerimiento`, `estadoRequerimiento`) VALUES ('3', 'Finalizado');

INSERT INTO `db_controlProyecto`.`prueba_estadoprueba` (`idEstadoPrueba`, `estadoPrueba`) VALUES ('1', 'Pendiente');
INSERT INTO `db_controlProyecto`.`prueba_estadoprueba` (`idEstadoPrueba`, `estadoPrueba`) VALUES ('2', 'Cumplido');
INSERT INTO `db_controlProyecto`.`prueba_estadoprueba` (`idEstadoPrueba`, `estadoPrueba`) VALUES ('3', 'Finalizado');

INSERT INTO db_controlProyecto.bug_clasificacion (clasificacion)
VALUES
  ('error'),
  ('mejora'),
  ('tarea');
  
UPDATE `db_controlProyecto`.`bug_clasificacion` SET `clasificacion` = 'Error' WHERE (`idClasificacion` = '1');
UPDATE `db_controlProyecto`.`bug_clasificacion` SET `clasificacion` = 'Mejora' WHERE (`idClasificacion` = '2');
UPDATE `db_controlProyecto`.`bug_clasificacion` SET `clasificacion` = 'Tarea' WHERE (`idClasificacion` = '3');

INSERT INTO `db_controlProyecto`.`bug_estadobug` (`idEstadoBug`, `estadoBug`) VALUES ('1', 'Abierto');
INSERT INTO `db_controlProyecto`.`bug_estadobug` (`idEstadoBug`, `estadoBug`) VALUES ('2', 'En progreso');
INSERT INTO `db_controlProyecto`.`bug_estadobug` (`idEstadoBug`, `estadoBug`) VALUES ('3', 'Cerrado');

####################################################################
#				TRIGGERS			   #
####################################################################
USE db_controlProyecto;
DELIMITER $$
DROP TRIGGER IF EXISTS proyecto_AFTER_UPDATE$$
CREATE DEFINER = CURRENT_USER TRIGGER `proyecto_AFTER_UPDATE` AFTER UPDATE ON `proyecto_proyecto` FOR EACH ROW
BEGIN
	IF OLD.idEstadoProyecto_id <> NEW.idEstadoProyecto_id THEN
		INSERT INTO proyecto_logestadoproyecto(idUsuarioRegistro_id, fechaRegistro, idProyecto_id, idEstadoProyecto_id)
        VALUES (OLD.idUsuariEncargado_id, NOW(), NEW.idProyecto, NEW.idEstadoProyecto_id);
    END IF;
END$$


DROP TRIGGER IF EXISTS `db_controlProyecto`.`prueba_prueba_AFTER_UPDATE`;

DELIMITER $$
USE `db_controlProyecto`$$
CREATE DEFINER = CURRENT_USER TRIGGER `db_controlProyecto`.`prueba_prueba_AFTER_UPDATE` AFTER UPDATE ON `prueba_prueba` FOR EACH ROW
BEGIN
	IF NEW.idEstadoPrueba_id <> OLD.idEstadoPrueba_id THEN
		INSERT INTO prueba_logestadoprueba(idEstadoPrueba_id, idPrueba_id, idUsuarioRegistro_id)
        VALUES(OLD.idEstadoPrueba_id, OLD.idPrueba, OLD.idUsuarioRegistro_id);
    END IF;
END$$
DELIMITER ;

