# Interdimensional summoning

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run execute as @a at @e[name="Compass"] run particle minecraft:squid_ink ~ ~1 ~9 7 7 7 .1 9000

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run execute as @a at @e[name="Compass"] run playsound minecraft:block.beacon.power_select block @s

# Copy terrain

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill 0 248 0 4 248 6 bedrock

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run clone ~-2 ~-2 ~2 ~2 ~3 ~8 0 249 0


# Start placing tent

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~ ~-1 ~4 ~ ~-1 ~5 minecraft:black_concrete replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~ ~2 ~3 ~ ~2 ~6 minecraft:red_wool replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~-1 ~3 minecraft:brown_wool replace

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~-1 ~1 ~3 ~-1 ~1 ~6 minecraft:red_wool replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~1 ~1 ~3 ~1 ~1 ~6 minecraft:red_wool replace

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~-1 ~ ~3 ~-1 ~ ~6 minecraft:red_wool replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~1 ~ ~3 ~1 ~ ~6 minecraft:red_wool replace

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~-2 ~ ~3 ~-2 ~ ~6 minecraft:red_wool replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~2 ~ ~3 ~2 ~ ~6 minecraft:red_wool replace

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~1 ~7 minecraft:red_wool replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~-1 ~ ~7 ~1 ~ ~7 minecraft:red_wool replace

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~ ~8 minecraft:red_wool replace

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~ ~1 ~5 ~ ~1 ~4 minecraft:black_concrete replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~-1 ~ ~4 ~-1 ~ ~5 minecraft:black_concrete replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run fill ~1 ~ ~4 ~1 ~ ~5 minecraft:black_concrete replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~1 ~6 minecraft:red_wool replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~-1 ~6 minecraft:brown_wool replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~1 ~3 minecraft:red_wool replace
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~ ~2 minecraft:spruce_trapdoor[facing=north, half=top, open=true]
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~ ~6 minecraft:spruce_trapdoor[facing=north, half=top, open=true]

execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run setblock ~ ~-2 ~5 minecraft:structure_block
execute as @a at @e[name=Compass] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name=Compass] run summon minecraft:armor_stand ~ ~ ~6 {Tags:["tent_pos"],CustomName:"\"tp_armorstand_1\"",Invisible:1}

tag @e[name=tp_armorstand_1] add south
