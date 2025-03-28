CREATE TABLE IF NOT EXISTS `character_item_reuse_save` (
  `charId` INT NOT NULL default 0,
  `itemId` INT NOT NULL default 0,
  `itemObjId` INT(3) NOT NULL default 1,
  `reuseDelay` INT(8) NOT NULL DEFAULT 0,
  `systime` BIGINT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (`charId`,`itemId`,`itemObjId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;