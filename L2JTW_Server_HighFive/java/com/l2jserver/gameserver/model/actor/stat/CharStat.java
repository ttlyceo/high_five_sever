/*
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation, either version 3 of the License, or (at your option) any later
 * version.
 * 
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.
 * 
 * You should have received a copy of the GNU General Public License along with
 * this program. If not, see <http://www.gnu.org/licenses/>.
 */
package com.l2jserver.gameserver.model.actor.stat;

import com.l2jserver.Config;
import com.l2jserver.gameserver.model.Elementals;
import com.l2jserver.gameserver.model.actor.L2Character;
import com.l2jserver.gameserver.model.items.L2Weapon;
import com.l2jserver.gameserver.model.items.instance.L2ItemInstance;
import com.l2jserver.gameserver.model.items.type.L2WeaponType;
import com.l2jserver.gameserver.model.skills.L2Skill;
import com.l2jserver.gameserver.model.stats.Calculator;
import com.l2jserver.gameserver.model.stats.Env;
import com.l2jserver.gameserver.model.stats.Stats;

public class CharStat
{
	private L2Character _activeChar;
	private long _exp = 0;
	private int _sp = 0;
	private byte _level = 1;
	
	public CharStat(L2Character activeChar)
	{
		_activeChar = activeChar;
	}
	
	/**
	 * Calculate the new value of the state with modifiers that will be applied
	 * on the targeted L2Character.<BR>
	 * <BR>
	 *
	 * <B><U> Concept</U> :</B><BR>
	 * <BR>
	 * A L2Character owns a table of Calculators called <B>_calculators</B>.
	 * Each Calculator (a calculator per state) own a table of Func object. A
	 * Func object is a mathematic function that permit to calculate the
	 * modifier of a state (ex : REGENERATE_HP_RATE...) : <BR>
	 * <BR>
	 *
	 * FuncAtkAccuracy -> Math.sqrt(_player.getDEX())*6+_player.getLevel()<BR>
	 * <BR>
	 *
	 * When the calc method of a calculator is launched, each mathematic
	 * function is called according to its priority <B>_order</B>. Indeed, Func
	 * with lowest priority order is executed firsta and Funcs with the same
	 * order are executed in unspecified order. The result of the calculation is
	 * stored in the value property of an Env class instance.<BR>
	 * <BR>
	 *
	 * @param stat
	 *            The stat to calculate the new value with modifiers
	 * @param init
	 *            The initial value of the stat before applying modifiers
	 * @param target
	 *            The L2Charcater whose properties will be used in the
	 *            calculation (ex : CON, INT...)
	 * @param skill
	 *            The L2Skill whose properties will be used in the calculation
	 *            (ex : Level...)
	 * @return 
	 */
	public final double calcStat(Stats stat, double init, L2Character target, L2Skill skill)
	{
		if (_activeChar == null || stat == null)
			return init;
		
		int id = stat.ordinal();
		
		Calculator c = _activeChar.getCalculators()[id];
		
		// If no Func object found, no modifier is applied
		if (c == null || c.size() == 0)
			return init;
		
		// Create and init an Env object to pass parameters to the Calculator
		Env env = new Env();
		env.setCharacter(_activeChar);
		env.setTarget(target);
		env.setSkill(skill);
		env.setValue(init);
		
		// Launch the calculation
		c.calc(env);
		// avoid some troubles with negative stats (some stats should never be negative)
		if (env.getValue() <= 0)
		{
			switch(stat)
			{
				case MAX_HP:
				case MAX_MP:
				case MAX_CP:
				case MAGIC_DEFENCE:
				case POWER_DEFENCE:
				case POWER_ATTACK:
				case MAGIC_ATTACK:
				case POWER_ATTACK_SPEED:
				case MAGIC_ATTACK_SPEED:
				case SHIELD_DEFENCE:
				case STAT_CON:
				case STAT_DEX:
				case STAT_INT:
				case STAT_MEN:
				case STAT_STR:
				case STAT_WIT:
					env.setValue(1);
			}
		}
		return env.getValue();
	}
	
	/**
	 * @return the Accuracy (base+modifier) of the L2Character in function of the Weapon Expertise Penalty.
	 */
	public int getAccuracy()
	{
		if (_activeChar == null)
			return 0;
		return (int) Math.round(calcStat(Stats.ACCURACY_COMBAT, 0, null, null));
	}
	
	public L2Character getActiveChar()
	{
		return _activeChar;
	}
	
	/**
	 * @return the Attack Speed multiplier (base+modifier) of the L2Character to get proper animations.
	 */
	public final float getAttackSpeedMultiplier()
	{
		if (_activeChar == null)
			return 1;
		
		return (float) ((1.1) * getPAtkSpd() / _activeChar.getTemplate().getBasePAtkSpd());
	}
	
	/**
	 * @return the CON of the L2Character (base+modifier).
	 */
	public final int getCON()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.STAT_CON, _activeChar.getTemplate().getBaseCON(), null, null);
	}
	
	/**
	 * @param target 
	 * @param init 
	 * @return the Critical Damage rate (base+modifier) of the L2Character.
	 */
	public final double getCriticalDmg(L2Character target, double init)
	{
		return calcStat(Stats.CRITICAL_DAMAGE, init, target, null);
	}
	
	/**
	 * @param target 
	 * @param skill 
	 * @return the Critical Hit rate (base+modifier) of the L2Character.
	 */
	public int getCriticalHit(L2Character target, L2Skill skill)
	{
		if (_activeChar == null)
			return 1;
		
		int criticalHit = (int) Math.round(calcStat(Stats.CRITICAL_RATE, _activeChar.getTemplate().getBaseCritRate(), target, skill)*10.0 + 0.5);
		criticalHit /= 10;
		// Set a cap of Critical Hit at 500
		if (criticalHit > Config.MAX_PCRIT_RATE)
			criticalHit = Config.MAX_PCRIT_RATE;
		
		return criticalHit;
	}
	
	/**
	 * @return the DEX of the L2Character (base+modifier).
	 */
	public final int getDEX()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.STAT_DEX, _activeChar.getTemplate().getBaseDEX(), null, null);
	}
	
	/**
	 * @param target 
	 * @return the Attack Evasion rate (base+modifier) of the L2Character.
	 */
	public int getEvasionRate(L2Character target)
	{
		if (_activeChar == null)
			return 1;
		
		int val = (int) Math.round(calcStat(Stats.EVASION_RATE, 0, target, null));
		if (val > Config.MAX_EVASION && !_activeChar.isGM())
			val = Config.MAX_EVASION;
		return val;
	}
	
	public long getExp()
	{
		return _exp;
	}
	
	public void setExp(long value)
	{
		_exp = value;
	}
	
	/**
	 * @return the INT of the L2Character (base+modifier).
	 */
	public int getINT()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.STAT_INT, _activeChar.getTemplate().getBaseINT(), null, null);
	}
	
	public byte getLevel()
	{
		return _level;
	}
	
	public void setLevel(byte value)
	{
		_level = value;
	}
	
	/**
	 * @param skill 
	 * @return the Magical Attack range (base+modifier) of the L2Character.
	 */
	public final int getMagicalAttackRange(L2Skill skill)
	{
		if (_activeChar == null)
			return 1;
		
		if (skill != null)
			return (int) calcStat(Stats.MAGIC_ATTACK_RANGE, skill.getCastRange(), null, skill);
		
		return _activeChar.getTemplate().getBaseAtkRange();
	}
	
	public int getMaxCp()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.MAX_CP, _activeChar.getTemplate().getBaseCpMax(), null, null);
	}
	
	public int getMaxRecoverableCp()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.MAX_RECOVERABLE_CP, getMaxCp(), null, null);
	}
	
	public int getMaxHp()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.LIMIT_HP, getMaxVisibleHp(), null, null);
	}
	
	public int getMaxVisibleHp()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.MAX_HP, _activeChar.getTemplate().getBaseHpMax(), null, null);
	}
	
	public int getMaxRecoverableHp()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.MAX_RECOVERABLE_HP, getMaxVisibleHp(), null, null);
	}
	
	public int getMaxMp()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.MAX_MP, _activeChar.getTemplate().getBaseMpMax(), null, null);
	}
	
	public int getMaxRecoverableMp()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.MAX_RECOVERABLE_MP, getMaxMp(), null, null);
	}
	
	/**
	 * Return the MAtk (base+modifier) of the L2Character for a skill used in
	 * function of abnormal effects in progress.<BR>
	 * <BR>
	 *
	 * <B><U> Example of use </U> :</B><BR>
	 * <BR>
	 * <li> Calculate Magic damage </li>
	 * <BR>
	 * <BR>
	 *
	 * @param target The L2Character targeted by the skill
	 * @param skill The L2Skill used against the target
	 * @return 
	 */
	public int getMAtk(L2Character target, L2Skill skill)
	{
		if (_activeChar == null)
			return 1;
		float bonusAtk = 1;
		if (Config.L2JMOD_CHAMPION_ENABLE && _activeChar.isChampion())
			bonusAtk = Config.L2JMOD_CHAMPION_ATK;
		if (_activeChar.isRaid())
			bonusAtk *= Config.RAID_MATTACK_MULTIPLIER;
		double attack = _activeChar.getTemplate().getBaseMAtk() * bonusAtk;
		// Get the skill type to calculate its effect in function of base stats
		// of the L2Character target
		Stats stat = skill == null ? null : skill.getStat();
		
		if (stat != null)
		{
			switch (stat)
			{
				case AGGRESSION:
					attack += _activeChar.getTemplate().getBaseAggression();
					break;
				case BLEED:
					attack += _activeChar.getTemplate().getBaseBleed();
					break;
				case POISON:
					attack += _activeChar.getTemplate().getBasePoison();
					break;
				case STUN:
					attack += _activeChar.getTemplate().getBaseStun();
					break;
				case ROOT:
					attack += _activeChar.getTemplate().getBaseRoot();
					break;
				case MOVEMENT:
					attack += _activeChar.getTemplate().getBaseMovement();
					break;
				case CONFUSION:
					attack += _activeChar.getTemplate().getBaseConfusion();
					break;
				case SLEEP:
					attack += _activeChar.getTemplate().getBaseSleep();
					break;
			}
		}
		
		// Add the power of the skill to the attack effect
		if (skill != null)
			attack += skill.getPower();
		
		// Calculate modifiers Magic Attack
		return (int) calcStat(Stats.MAGIC_ATTACK, attack, target, skill);
	}
	
	/**
	 * @return the MAtk Speed (base+modifier) of the L2Character in function of the Armour Expertise Penalty.
	 */
	public int getMAtkSpd()
	{
		if (_activeChar == null)
			return 1;
		float bonusSpdAtk = 1;
		if  (Config.L2JMOD_CHAMPION_ENABLE && _activeChar.isChampion())
			bonusSpdAtk = Config.L2JMOD_CHAMPION_SPD_ATK;
		double val = calcStat(Stats.MAGIC_ATTACK_SPEED, _activeChar.getTemplate().getBaseMAtkSpd() * bonusSpdAtk, null, null);
		if (val > Config.MAX_MATK_SPEED && !_activeChar.isGM())
			val = Config.MAX_MATK_SPEED;
		return (int) val;
	}
	
	/**
	 * @param target 
	 * @param skill 
	 * @return the Magic Critical Hit rate (base+modifier) of the L2Character.
	 */
	public final int getMCriticalHit(L2Character target, L2Skill skill)
	{
		if (_activeChar == null)
			return 1;
		
		double mrate = calcStat(Stats.MCRITICAL_RATE, _activeChar.getTemplate().getBaseMCritRate(), target, skill);
		if(mrate > Config.MAX_MCRIT_RATE)
			mrate = Config.MAX_MCRIT_RATE;
		return (int) mrate;
	}
	
	/**
	 * <B><U> Example of use </U> :</B><BR>
	 * <BR>
	 * <li> Calculate Magic damage </li>
	 * <BR>
	 *
	 * @param target
	 *            The L2Character targeted by the skill
	 * @param skill
	 *            The L2Skill used against the target
	 * @return the MDef (base+modifier) of the L2Character against a skill in function of abnormal effects in progress.
	 */
	public int getMDef(L2Character target, L2Skill skill)
	{
		if (_activeChar == null)
			return 1;
		
		// Get the base MAtk of the L2Character
		double defence = _activeChar.getTemplate().getBaseMDef();
		
		// Calculate modifier for Raid Bosses
		if (_activeChar.isRaid())
			defence *= Config.RAID_MDEFENCE_MULTIPLIER;
		
		// Calculate modifiers Magic Attack
		return (int) calcStat(Stats.MAGIC_DEFENCE, defence, target, skill);
	}
	
	/**
	 * @return the MEN of the L2Character (base+modifier).
	 */
	public final int getMEN()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.STAT_MEN, _activeChar.getTemplate().getBaseMEN(), null, null);
	}
	
	public float getMovementSpeedMultiplier()
	{
		if (_activeChar == null)
			return 1;
		
		return getRunSpeed() / (float) _activeChar.getTemplate().getBaseRunSpd();
	}
	
	/**
	 * @return the RunSpeed (base+modifier) or WalkSpeed (base+modifier) of the L2Character in function of the movement type.
	 */
	public float getMoveSpeed()
	{
		if (_activeChar == null)
			return 1;
		
		if (_activeChar.isRunning())
			return getRunSpeed();
		return getWalkSpeed();
	}
	
	/**
	 * @param skill 
	 * @return the MReuse rate (base+modifier) of the L2Character.
	 */
	public final double getMReuseRate(L2Skill skill)
	{
		if (_activeChar == null)
			return 1;
		
		return calcStat(Stats.MAGIC_REUSE_RATE, _activeChar.getTemplate().getBaseMReuseRate(), null, skill);
	}
	
	/**
	 * @param target 
	 * @return the PAtk (base+modifier) of the L2Character.
	 */
	public int getPAtk(L2Character target)
	{
		if (_activeChar == null)
			return 1;
		float bonusAtk = 1;
		if  (Config.L2JMOD_CHAMPION_ENABLE && _activeChar.isChampion())
			bonusAtk = Config.L2JMOD_CHAMPION_ATK;
		if (_activeChar.isRaid())
			bonusAtk *= Config.RAID_PATTACK_MULTIPLIER;
		return (int) calcStat(Stats.POWER_ATTACK, _activeChar.getTemplate().getBasePAtk() * bonusAtk, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PAtk Modifier against animals.
	 */
	public final double getPAtkAnimals(L2Character target)
	{
		return calcStat(Stats.PATK_ANIMALS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PAtk Modifier against dragons.
	 */
	public final double getPAtkDragons(L2Character target)
	{
		return calcStat(Stats.PATK_DRAGONS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PAtk Modifier against insects.
	 */
	public final double getPAtkInsects(L2Character target)
	{
		return calcStat(Stats.PATK_INSECTS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PAtk Modifier against monsters.
	 */
	public final double getPAtkMonsters(L2Character target)
	{
		return calcStat(Stats.PATK_MONSTERS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PAtk Modifier against plants.
	 */
	public final double getPAtkPlants(L2Character target)
	{
		return calcStat(Stats.PATK_PLANTS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PAtk Modifier against giants.
	 */
	public final double getPAtkGiants(L2Character target)
	{
		return calcStat(Stats.PATK_GIANTS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PAtk Modifier against magic creatures.
	 */
	public final double getPAtkMagicCreatures(L2Character target)
	{
		return calcStat(Stats.PATK_MCREATURES, 1, target, null);
	}
	/**
	 * @return the PAtk Speed (base+modifier) of the L2Character in function of the Armour Expertise Penalty.
	 */
	public int getPAtkSpd()
	{
		if (_activeChar == null)
			return 1;
		float bonusAtk = 1;
		if  (Config.L2JMOD_CHAMPION_ENABLE && _activeChar.isChampion())
			bonusAtk = Config.L2JMOD_CHAMPION_SPD_ATK;
		int val = (int) Math.round(calcStat(Stats.POWER_ATTACK_SPEED, _activeChar.getTemplate().getBasePAtkSpd() * bonusAtk, null, null));
		return val;
	}
	
	/**
	 * @param target 
	 * @return the PDef Modifier against animals.
	 */
	public final double getPDefAnimals(L2Character target)
	{
		return calcStat(Stats.PDEF_ANIMALS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PDef Modifier against dragons.
	 */
	public final double getPDefDragons(L2Character target)
	{
		return calcStat(Stats.PDEF_DRAGONS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PDef Modifier against insects.
	 */
	public final double getPDefInsects(L2Character target)
	{
		return calcStat(Stats.PDEF_INSECTS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PDef Modifier against monsters.
	 */
	public final double getPDefMonsters(L2Character target)
	{
		return calcStat(Stats.PDEF_MONSTERS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PDef Modifier against plants.
	 */
	public final double getPDefPlants(L2Character target)
	{
		return calcStat(Stats.PDEF_PLANTS, 1, target, null);
	}
	
	/**
	 * @param target 
	 * @return the PDef Modifier against giants.
	 */
	public final double getPDefGiants(L2Character target)
	{
		return calcStat(Stats.PDEF_GIANTS, 1, target, null);
	}

	/**
	 * @param target 
	 * @return the PDef Modifier against giants.
	 */
	public final double getPDefMagicCreatures(L2Character target)
	{
		return calcStat(Stats.PDEF_MCREATURES, 1, target, null);
	}

	/**
	 * @param target 
	 * @return the PDef (base+modifier) of the L2Character.
	 */
	public int getPDef(L2Character target)
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.POWER_DEFENCE, (_activeChar.isRaid()) ? _activeChar.getTemplate().getBasePDef() * Config.RAID_PDEFENCE_MULTIPLIER : _activeChar.getTemplate().getBasePDef(), target, null);
	}
	
	/**
	 * @return the Physical Attack range (base+modifier) of the L2Character.
	 */
	public final int getPhysicalAttackRange()
	{
		if (_activeChar == null)
			return 1;
		
		if (_activeChar.isTransformed())
			return _activeChar.getTemplate().getBaseAtkRange();
		// Polearm handled here for now. Basically L2PcInstance could have a function
		// similar to FuncBowAtkRange and NPC are defined in DP.
		L2Weapon weaponItem = _activeChar.getActiveWeaponItem();
		if (weaponItem != null && weaponItem.getItemType() == L2WeaponType.POLE)
			return (int) calcStat(Stats.POWER_ATTACK_RANGE, 66, null, null);
		
		return (int) calcStat(Stats.POWER_ATTACK_RANGE, _activeChar.getTemplate().getBaseAtkRange(), null, null);
	}
	
	/**
	 * @param target 
	 * @return the weapon reuse modifier.
	 */
	public final double getWeaponReuseModifier(L2Character target)
	{
		return calcStat(Stats.ATK_REUSE, 1, target, null);
	}
	
	/**
	 * @return the RunSpeed (base+modifier) of the L2Character in function of the Armour Expertise Penalty.
	 */
	public int getRunSpeed()
	{
		if (_activeChar == null)
			return 1;
		
		// err we should be adding TO the persons run speed
		// not making it a constant
		double baseRunSpd = _activeChar.getTemplate().getBaseRunSpd();
		
		if (baseRunSpd == 0)
			return 0;
		
		return (int) Math.round(calcStat(Stats.RUN_SPEED, baseRunSpd, null, null));
	}
	
	/**
	 * @return the ShieldDef rate (base+modifier) of the L2Character.
	 */
	public final int getShldDef()
	{
		return (int) calcStat(Stats.SHIELD_DEFENCE, 0, null, null);
	}
	
	public int getSp()
	{
		return _sp;
	}
	
	public void setSp(int value)
	{
		_sp = value;
	}
	
	/**
	 * @return the STR of the L2Character (base+modifier).
	 */
	public final int getSTR()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.STAT_STR, _activeChar.getTemplate().getBaseSTR(), null, null);
	}
	
	/**
	 * @return the WalkSpeed (base+modifier) of the L2Character.
	 */
	public int getWalkSpeed()
	{
		if (_activeChar == null)
			return 1;
		
		double baseWalkSpd = _activeChar.getTemplate().getBaseWalkSpd();
		
		if (baseWalkSpd == 0)
			return 0;
		
		return (int) calcStat(Stats.WALK_SPEED, baseWalkSpd, null, null);
	}
	
	/**
	 * @return the WIT of the L2Character (base+modifier).
	 */
	public final int getWIT()
	{
		if (_activeChar == null)
			return 1;
		
		return (int) calcStat(Stats.STAT_WIT, _activeChar.getTemplate().getBaseWIT(), null, null);
	}
	
	/**
	 * @param skill 
	 * @return the mpConsume.
	 */
	public final int getMpConsume(L2Skill skill)
	{
		if (skill == null)
			return 1;
		double mpConsume = skill.getMpConsume();
		double nextDanceMpCost = Math.ceil(skill.getMpConsume() / 2.);
		if (skill.isDance())
		{
			if (Config.DANCE_CONSUME_ADDITIONAL_MP
					&& _activeChar != null
					&& _activeChar.getDanceCount() > 0)
				mpConsume += _activeChar.getDanceCount() * nextDanceMpCost;
		}
		
		mpConsume = calcStat(Stats.MP_CONSUME, mpConsume, null, skill);
		
		if (skill.isDance())
			return (int)calcStat(Stats.DANCE_MP_CONSUME_RATE, mpConsume, null, null);
		else if (skill.isMagic())
			return (int)calcStat(Stats.MAGICAL_MP_CONSUME_RATE, mpConsume, null, null);
		else
			return (int)calcStat(Stats.PHYSICAL_MP_CONSUME_RATE, mpConsume, null, null);
	}
	
	/**
	 * @param skill 
	 * @return the mpInitialConsume.
	 */
	public final int getMpInitialConsume(L2Skill skill)
	{
		if (skill == null)
			return 1;
		
		double mpConsume = calcStat(Stats.MP_CONSUME, skill.getMpInitialConsume(), null, skill);
		
		if (skill.isDance())
			return (int)calcStat(Stats.DANCE_MP_CONSUME_RATE, mpConsume, null, null);
		else if (skill.isMagic())
			return (int)calcStat(Stats.MAGICAL_MP_CONSUME_RATE, mpConsume, null, null);
		else
			return (int)calcStat(Stats.PHYSICAL_MP_CONSUME_RATE, mpConsume, null, null);
	}
	
	public byte getAttackElement()
	{
		L2ItemInstance weaponInstance = _activeChar.getActiveWeaponInstance();
		// 1st order - weapon element
		if (weaponInstance != null && weaponInstance.getAttackElementType() >= 0 )
			return weaponInstance.getAttackElementType();
		
		// temp fix starts
		int tempVal =0, stats[] = { 0, 0, 0, 0, 0, 0 };
		
		byte returnVal = -2;
		stats[0] = (int) calcStat(Stats.FIRE_POWER, _activeChar.getTemplate().getBaseFire(), null, null);
		stats[1] = (int) calcStat(Stats.WATER_POWER, _activeChar.getTemplate().getBaseWater(), null, null);
		stats[2] = (int) calcStat(Stats.WIND_POWER, _activeChar.getTemplate().getBaseWind(), null, null);
		stats[3] = (int) calcStat(Stats.EARTH_POWER, _activeChar.getTemplate().getBaseEarth(), null, null);
		stats[4] = (int) calcStat(Stats.HOLY_POWER, _activeChar.getTemplate().getBaseHoly(), null, null);
		stats[5] = (int) calcStat(Stats.DARK_POWER, _activeChar.getTemplate().getBaseDark(), null, null);
		
		for (byte x = 0; x < 6; x++)
		{
			if (stats[x] > tempVal)
			{
				returnVal = x;
				tempVal = stats[x];
			}
		}
		
		return returnVal;
		// temp fix ends
		
		/*
		 * uncomment me once deadlocks in getAllEffects() fixed
			return _activeChar.getElementIdFromEffects();
		 */
	}
	
	public int getAttackElementValue(byte attackAttribute)
	{
		switch (attackAttribute)
		{
			case Elementals.FIRE:
				return (int) calcStat(Stats.FIRE_POWER, _activeChar.getTemplate().getBaseFire(), null, null);
			case Elementals.WATER:
				return (int) calcStat(Stats.WATER_POWER, _activeChar.getTemplate().getBaseWater(), null, null);
			case Elementals.WIND:
				return (int) calcStat(Stats.WIND_POWER, _activeChar.getTemplate().getBaseWind(), null, null);
			case Elementals.EARTH:
				return (int) calcStat(Stats.EARTH_POWER, _activeChar.getTemplate().getBaseEarth(), null, null);
			case Elementals.HOLY:
				return (int) calcStat(Stats.HOLY_POWER, _activeChar.getTemplate().getBaseHoly(), null, null);
			case Elementals.DARK:
				return (int) calcStat(Stats.DARK_POWER, _activeChar.getTemplate().getBaseDark(), null, null);
			default:
				return 0;
		}
	}
	
	public int getDefenseElementValue(byte defenseAttribute)
	{
		switch (defenseAttribute)
		{
			case Elementals.FIRE:
				return (int) calcStat(Stats.FIRE_RES, _activeChar.getTemplate().getBaseFireRes(), null, null);
			case Elementals.WATER:
				return (int) calcStat(Stats.WATER_RES, _activeChar.getTemplate().getBaseWaterRes(), null, null);
			case Elementals.WIND:
				return (int) calcStat(Stats.WIND_RES, _activeChar.getTemplate().getBaseWindRes(), null, null);
			case Elementals.EARTH:
				return (int) calcStat(Stats.EARTH_RES, _activeChar.getTemplate().getBaseEarthRes(), null, null);
			case Elementals.HOLY:
				return (int) calcStat(Stats.HOLY_RES, _activeChar.getTemplate().getBaseHolyRes(), null, null);
			case Elementals.DARK:
				return (int) calcStat(Stats.DARK_RES, _activeChar.getTemplate().getBaseDarkRes(), null, null);
			default:
				return 0;
		}
	}
}
