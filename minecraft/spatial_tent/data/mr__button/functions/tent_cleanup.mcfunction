#South Cleanup
execute if entity @e[name=tp_armorstand_1] positioned ~ ~ ~6 at @e[name="Ender Pearl"] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name="Ender Pearl"] run execute as @a at @e[name="Ender Pearl"] run particle minecraft:squid_ink ~ ~1 ~9 7 7 7 .1 9000

execute if entity @e[name=tp_armorstand_1] positioned ~ ~ ~6 at @e[name="Ender Pearl"] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name="Ender Pearl"] run execute as @a at @e[name="Ender Pearl"] run playsound minecraft:block.beacon.power_select master @s ~ ~ ~ 0.5 2

execute if entity @e[name=tp_armorstand_1] positioned ~ ~ ~6 at @e[name='Ender Pearl'] if block ~ ~ ~ minecraft:campfire if entity @s[y_rotation=-45..45] run execute in spatial_tent:spatial_tent run clone 0 249 0 4 254 6 ~-2 ~-2 ~2


#North Cleanup
execute if entity @e[name=tp_armorstand_1] positioned ~ ~ ~-6 at @e[name="Ender Pearl"] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name="Ender Pearl"] run execute as @a at @e[name="Ender Pearl"] run particle minecraft:squid_ink ~ ~1 ~-9 7 7 7 .1 9000

execute if entity @e[name=tp_armorstand_1] positioned ~ ~ ~-6 at @e[name="Ender Pearl"] if block ~ ~ ~ minecraft:campfire facing entity @p eyes at @e[name="Ender Pearl"] run execute as @a at @e[name="Ender Pearl"] run playsound minecraft:block.beacon.power_select master @s ~ ~ ~ 0.5 2

execute if entity @e[name=tp_armorstand_1] positioned ~ ~ ~-6 at @e[name='Ender Pearl'] if block ~ ~ ~ minecraft:campfire if entity @s[y_rotation=135..225] run execute in spatial_tent:spatial_tent run clone 0 249 0 4 254 6 ~-2 ~-2 ~-8

kill @e[name=tp_armorstand_1]
kill @e[name=tp_armorstand_2]
kill @e[tag=tent_pos]
