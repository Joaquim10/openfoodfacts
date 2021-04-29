-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema openfoodfacts
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `openfoodfacts` ;
USE `openfoodfacts` ;

-- -----------------------------------------------------
-- Table `openfoodfacts`.`Category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfoodfacts`.`Category` ;

CREATE TABLE IF NOT EXISTS `openfoodfacts`.`Category` (
  `category_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NOT NULL,
  PRIMARY KEY (`category_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openfoodfacts`.`Product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfoodfacts`.`Product` ;

CREATE TABLE IF NOT EXISTS `openfoodfacts`.`Product` (
  `product_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(400) NOT NULL,
  `category_id` INT UNSIGNED NOT NULL,
  `description` VARCHAR(400) NULL DEFAULT NULL,
  `nutri_score` CHAR(1) NOT NULL,
  `stores` VARCHAR(400) NULL,
  `url` VARCHAR(400) NOT NULL,
  PRIMARY KEY (`product_id`),
  INDEX `fk_Product_Category1_idx` (`category_id` ASC),
  CONSTRAINT `fk_Product_Category1`
    FOREIGN KEY (`category_id`)
    REFERENCES `openfoodfacts`.`Category` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `openfoodfacts`.`Substitute`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `openfoodfacts`.`Substitute` ;

CREATE TABLE IF NOT EXISTS `openfoodfacts`.`Substitute` (
  `product_id` INT UNSIGNED NOT NULL,
  `substitute_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`product_id`, `substitute_id`),
  INDEX `fk_Product_has_Product_Product2_idx` (`substitute_id` ASC),
  INDEX `fk_Product_has_Product_Product1_idx` (`product_id` ASC),
  CONSTRAINT `fk_Product_has_Product_Product1`
    FOREIGN KEY (`product_id`)
    REFERENCES `openfoodfacts`.`Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Product_has_Product_Product2`
    FOREIGN KEY (`substitute_id`)
    REFERENCES `openfoodfacts`.`Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
