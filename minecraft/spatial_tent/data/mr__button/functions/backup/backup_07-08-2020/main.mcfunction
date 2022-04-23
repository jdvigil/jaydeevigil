# South Cleanup

execute as @a at @e[name='Ender Pearl'] if block ~ ~ ~ minecraft:campfire run function spatial_tent:tent_cleanup


# Spatial Tent Setup South

execute unless entity @e[name=tp_armorstand_1] as @a at @e[name=Compass] if entity @s[y_rotation=-45..45] if block ~ ~ ~ minecraft:campfire run function spatial_tent:spatial_tent_south


# Spatial Tent Setup North

execute unless entity @e[name=tp_armorstand_1] as @a at @e[name=Compass] if entity @s[y_rotation=135..225] if block ~ ~ ~ minecraft:campfire run function spatial_tent:spatial_tent_north


# TP from spatial tent to overworld
# Find a way to retrieve scoreboard data. 

# South
execute as @a at @s if block ~ ~-2 ~ minecraft:jigsaw if entity @s[y_rotation=-135..-46] run execute as @a at @e[name=tp_armorstand_1] if entity @e[name=tp_armorstand_2] positioned ~ ~ ~3 run tp @s ~.5 ~ ~-4.7 180 0

# North
execute as @a at @s if block ~ ~-2 ~ minecraft:jigsaw if entity @s[y_rotation=-135..-46] run execute as @a at @e[name=tp_armorstand_1] if entity @e[name=tp_armorstand_2] positioned ~ ~ ~-3 run tp @s ~-.2 ~ ~4.5 0 0

# TP player to spatial tent


