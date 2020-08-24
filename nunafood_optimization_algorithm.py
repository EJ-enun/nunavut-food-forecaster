#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:42:54 2020

@author:Enun, Enun Jay
"""

import pandas as pd
import numpy as np 


df_community = pd.read_csv('/Users/cinema/Desktop/nunavut_communities_data.csv').fillna(0)

df_price_list = pd.read_csv('/Users/cinema/Desktop/fresh_produce_dataset.csv').fillna(0)


def getProducePriceMinOverhead(collectProduce, total):
    return collectProduce - total

#method for collecting a specific row in a column for a specific produce
def collectProduce(produce, produce_shelflife, produce_price_per_kg):
    df_produce = produce
    df_shelflife = float(produce_shelflife)
    df_produce_price = float(produce_price_per_kg)
    price_per_60000_kg = df_produce_price * 60000
    return price_per_60000_kg
#produce is moved 2 times a week. 

#get produce values from our fresh_produce_dataset.
product_type_beef = df_price_list['product_type_beef']
location_beef = df_price_list['location_beef']
price_per_one_kg_beef = df_price_list['price_per_one_kg_beef']
produce_lifetime_days_beef = df_price_list['produce_lifetime_days_beef']


product_type_dairy = df_price_list['product_type_dairy']
location_dairy = df_price_list['location_dairy']
price_per_one_kg_dairy = df_price_list['price_per_litre_kg']
produce_lifetime_days_dairy = df_price_list['produce_lifetime_days_dairy']


product_type_fruit = df_price_list['product_type_fruit']
location_fruit = df_price_list['location_fruit']
price_per_one_kg_fruit = df_price_list['price_per_kg_fruit']
produce_lifetime_days_fruit = df_price_list['produce_lifetime_days_fruit']


product_type_grain = df_price_list['product_type_grain']
location_grain = df_price_list['location_grain']
price_per_bushel_grain = df_price_list['price_per_bushel_grain']
produce_lifetime_days_grain = df_price_list['produce_lifetime_days_grain']


product_type_vegetables = df_price_list['product_type_vegetables']
location_vegetables = df_price_list['location_vegetables']
price_per_one_kg_vegetables = df_price_list['price_per_kg_vegetables']
produce_lifetime_days_vegetables = df_price_list['produce_lifetime_days_vegetables']

#overhead costs
personnel_cost = df_community['personnel_cost']
storage_cost = df_community['storage_cost']
air_freight_cost = df_community['freightfare_per_region_based_off_kg_of_food_allocated']

#assuming we make just one trip a month, overhead before produce acquisition. 
#Total values
p_c = personnel_cost[25]
s_c = storage_cost[25]
a_f_c = air_freight_cost[25]
total_overhead = np.stack([p_c,s_c,a_f_c], axis = 0)

total_overhead = 679279.16
total_kg = 60000
#monthly costs pre-produce acquisitionare 679,279.16

#produce cost for 60,000 KG worth of different produce. 
#beef

bacon = collectProduce(product_type_beef[0], produce_lifetime_days_beef[0], price_per_one_kg_beef[0])
blade_roast = collectProduce(product_type_beef[1], produce_lifetime_days_beef[1], price_per_one_kg_beef[1])
broiler_chicken = collectProduce(product_type_beef[2], produce_lifetime_days_beef[2], price_per_one_kg_beef[2])
ground_beef = collectProduce(product_type_beef[3], produce_lifetime_days_beef[3], price_per_one_kg_beef[3])
pork_chops = collectProduce(product_type_beef[4], produce_lifetime_days_beef[4], price_per_one_kg_beef[4])
prime_rib_roast = collectProduce(product_type_beef[5], produce_lifetime_days_beef[5], price_per_one_kg_beef[5])
round_steak = collectProduce(product_type_beef[6], produce_lifetime_days_beef[6], price_per_one_kg_beef[6])
sirloin_steak = collectProduce(product_type_beef[7], produce_lifetime_days_beef[7], price_per_one_kg_beef[7])
stewing_beef = collectProduce(product_type_beef[8], produce_lifetime_days_beef[8], price_per_one_kg_beef[8])
wieners = collectProduce(product_type_beef[9], produce_lifetime_days_beef[9], price_per_one_kg_beef[9])

#group all current retail prices of beef types into one list
beef = [bacon,blade_roast,broiler_chicken,ground_beef,pork_chops,prime_rib_roast,round_steak,sirloin_steak, stewing_beef, wieners]
 
#total overhead cost subtracted from the total cost of 60,000 kg of beef 
bacon_tot_min_overhead_cost = getProducePriceMinOverhead(bacon, total_overhead)
blade_roast_tot_min_overhead_cost = getProducePriceMinOverhead(blade_roast, total_overhead)
broiler_chicken_tot_min_overhead_cost = getProducePriceMinOverhead(broiler_chicken, total_overhead)
ground_beef_tot_min_overhead_cost = getProducePriceMinOverhead(ground_beef, total_overhead)
pork_chops_tot_min_overhead_cost = getProducePriceMinOverhead(pork_chops, total_overhead)
prime_rib_tot_min_overhead_cost = getProducePriceMinOverhead(prime_rib_roast, total_overhead)
round_steak_tot_min_overhead_cost = getProducePriceMinOverhead(round_steak, total_overhead)
sirloin_steak_tot_min_overhead_cost = getProducePriceMinOverhead(sirloin_steak, total_overhead)
stewing_beef_tot_min_overhead_cost = getProducePriceMinOverhead(stewing_beef, total_overhead)
wieners_tot_min_overhead_cost = getProducePriceMinOverhead(wieners, total_overhead)

produce_60k_kg_min_tot_overhead_costs_list = [bacon_tot_min_overhead_cost,blade_roast_tot_min_overhead_cost,broiler_chicken_tot_min_overhead_cost, ground_beef_tot_min_overhead_cost, pork_chops_tot_min_overhead_cost, prime_rib_tot_min_overhead_cost, round_steak_tot_min_overhead_cost, sirloin_steak_tot_min_overhead_cost, stewing_beef_tot_min_overhead_cost,wieners_tot_min_overhead_cost   ]

adj_bacon = getProducePriceMinOverhead(bacon, total_overhead) / total_kg
adj_blade_roast = getProducePriceMinOverhead(blade_roast, total_overhead) / total_kg
adj_broiler_chicken = getProducePriceMinOverhead(broiler_chicken, total_overhead) / total_kg
adj_ground_beef = getProducePriceMinOverhead(ground_beef, total_overhead) / total_kg
adj_pork_chops = getProducePriceMinOverhead(pork_chops, total_overhead) / total_kg
adj_prime_rib_roast = getProducePriceMinOverhead(prime_rib_roast, total_overhead) / total_kg
adj_round_steak = getProducePriceMinOverhead(round_steak, total_overhead) / total_kg
adj_sirloin_steak = getProducePriceMinOverhead(sirloin_steak, total_overhead) / total_kg
adj_stewing_beef = getProducePriceMinOverhead(stewing_beef, total_overhead) / total_kg
adj_wieners = getProducePriceMinOverhead(wieners, total_overhead) / total_kg

new_price_per_kg_of_produce = [adj_bacon,adj_blade_roast,adj_broiler_chicken,adj_ground_beef,adj_pork_chops,adj_prime_rib_roast,adj_round_steak,adj_sirloin_steak, adj_stewing_beef, adj_wieners]

new = [i/j for i,j in zip(new_price_per_kg_of_produce,beef)]


#dairy
chicken_eggs = collectProduce(product_type_dairy[0],produce_lifetime_days_dairy[0],price_per_one_kg_dairy[0])
milk = collectProduce(product_type_dairy[1],produce_lifetime_days_dairy[1],price_per_one_kg_dairy[1])

#total overhead cost subtracted from the total cost of 60,000 kg of dairy 
chicken_egg_min_overhead = getProducePriceMinOverhead(chicken_eggs, total_kg)
milk_min_overhead = getProducePriceMinOverhead(milk, total_kg)

#adjusted cost per unit of 60,000 kg of produce after subtracting overhead. 
adj_chicken_egg = chicken_egg_min_overhead / total_kg
adj_milk = milk_min_overhead / total_kg







#fruit
apple = collectProduce(product_type_fruit[0],produce_lifetime_days_fruit[0],price_per_one_kg_fruit[0])
apricot = collectProduce(product_type_fruit[1],produce_lifetime_days_fruit[1],price_per_one_kg_fruit[1]) 
avocado = collectProduce(product_type_fruit[2],produce_lifetime_days_fruit[2],price_per_one_kg_fruit[2])
banana = collectProduce(product_type_fruit[3],produce_lifetime_days_fruit[3],price_per_one_kg_fruit[3])
blueberry = collectProduce(product_type_fruit[4],produce_lifetime_days_fruit[4],price_per_one_kg_fruit[4])
cherries = collectProduce(product_type_fruit[5],produce_lifetime_days_fruit[5],price_per_one_kg_fruit[5])
cranberry = collectProduce(product_type_fruit[6],produce_lifetime_days_fruit[6],price_per_one_kg_fruit[6])
grapefruit = collectProduce(product_type_fruit[7],produce_lifetime_days_fruit[7],price_per_one_kg_fruit[7])
grapes = collectProduce(product_type_fruit[8],produce_lifetime_days_fruit[8],price_per_one_kg_fruit[8])
guava = collectProduce(product_type_fruit[9],produce_lifetime_days_fruit[9],price_per_one_kg_fruit[9])
orange = collectProduce(product_type_fruit[10],produce_lifetime_days_fruit[10],price_per_one_kg_fruit[10])
papaya = collectProduce(product_type_fruit[11],produce_lifetime_days_fruit[11],price_per_one_kg_fruit[11])
peach = collectProduce(product_type_fruit[12],produce_lifetime_days_fruit[12],price_per_one_kg_fruit[12])
pear = collectProduce(product_type_fruit[13],produce_lifetime_days_fruit[13],price_per_one_kg_fruit[13])

#total overhead cost subtracted from the total cost of 60,000 kg of fruit.
apple_min_overhead = getProducePriceMinOverhead(apple, total_kg)
apricot_min_overhead = getProducePriceMinOverhead(apricot, total_kg)
avocado_min_overhead = getProducePriceMinOverhead(avocado, total_kg)
banana_min_overhead = getProducePriceMinOverhead(banana, total_kg)
blueberry_min_overhead = getProducePriceMinOverhead(blueberry, total_kg)
cherries_min_overhead = getProducePriceMinOverhead(cherries, total_kg)
cranberry_min_overhead = getProducePriceMinOverhead(cranberry, total_kg)
grapefruit_min_overhead = getProducePriceMinOverhead(grapefruit, total_kg)
grapes_min_overhead = getProducePriceMinOverhead(grapes, total_kg)
guava_min_overhead = getProducePriceMinOverhead(guava, total_kg)
orange_min_overhead = getProducePriceMinOverhead(orange, total_kg)
papaya_min_overhead = getProducePriceMinOverhead(papaya, total_kg) 
peach_min_overhead = getProducePriceMinOverhead(peach, total_kg)
pear_min_overhead = getProducePriceMinOverhead(pear, total_kg)


#adjusted cost per unit of 60,000 kg of produce after subtracting overhead.

adj_apple = apple_min_overhead / total_kg
adj_apricot = apricot_min_overhead / total_kg
adj_avocado = avocado_min_overhead / total_kg
adj_banana = banana_min_overhead / total_kg
adj_blueberry = blueberry_min_overhead / total_kg
adj_cherries = cherries_min_overhead / total_kg
adj_cranberry = cranberry_min_overhead / total_kg
adj_grapefruit = grapefruit_min_overhead / total_kg
adj_grapes = grapes_min_overhead / total_kg
adj_guava = guava_min_overhead / total_kg
adj_orange = orange_min_overhead / total_kg
adj_papaya = papaya_min_overhead / total_kg
adj_peach = peach_min_overhead / total_kg
adj_pear = pear_min_overhead / total_kg


#grain
barley = collectProduce(product_type_grain[0],produce_lifetime_days_grain[0],price_per_bushel_grain[0])
canola = collectProduce(product_type_grain[1],produce_lifetime_days_grain[1],price_per_bushel_grain[1])
corn = collectProduce(product_type_grain[2],produce_lifetime_days_grain[2],price_per_bushel_grain[2])
flaxseed = collectProduce(product_type_grain[3],produce_lifetime_days_grain[3],price_per_bushel_grain[3])
oats = collectProduce(product_type_grain[4],produce_lifetime_days_grain[4],price_per_bushel_grain[4])
peas = collectProduce(product_type_grain[5],produce_lifetime_days_grain[5],price_per_bushel_grain[5])
soybean = collectProduce(product_type_grain[6],produce_lifetime_days_grain[6],price_per_bushel_grain[6])
wheat = collectProduce(product_type_grain[7],produce_lifetime_days_grain[7],price_per_bushel_grain[7])

#total overhead cost subtracted from the total cost of 60,000 kg of grain. 
barley_min_overhead = getProducePriceMinOverhead(barley, total_kg)
canola_min_overhead = getProducePriceMinOverhead(canola, total_kg)
corn_min_overhead = getProducePriceMinOverhead(corn, total_kg)
flaxseed_min_overhead = getProducePriceMinOverhead(flaxseed, total_kg)
oats_min_overhead = getProducePriceMinOverhead(oats, total_kg)
peas_min_overhead = getProducePriceMinOverhead(peas, total_kg)
soybean_min_overhead = getProducePriceMinOverhead(soybean, total_kg)
wheat_min_overhead = getProducePriceMinOverhead(wheat, total_kg)

#adjusted cost per unit of 60,000 kg of produce after subtracting overhead.

barley = barley_min_overhead / total_kg
canola = canola_min_overhead / total_kg
corn = corn_min_overhead / total_kg
flaxseed = flaxseed_min_overhead / total_kg
oats = oats_min_overhead / total_kg
peas = peas_min_overhead / total_kg
soybean = soybean_min_overhead / total_kg
wheat = wheat_min_overhead / total_kg


#vegetables
artichoke = collectProduce(product_type_vegetables[0],produce_lifetime_days_vegetables[0],price_per_one_kg_vegetables[0])
asparagus = collectProduce(product_type_vegetables[1],produce_lifetime_days_vegetables[1],price_per_one_kg_vegetables[1])
garlic = collectProduce(product_type_vegetables[2],produce_lifetime_days_vegetables[2],price_per_one_kg_vegetables[2])
green_beans = collectProduce(product_type_vegetables[3],produce_lifetime_days_vegetables[3],price_per_one_kg_vegetables[3])
beets = collectProduce(product_type_vegetables[4],produce_lifetime_days_vegetables[4],price_per_one_kg_vegetables[4])
bell_peppers = collectProduce(product_type_vegetables[5],produce_lifetime_days_vegetables[5],price_per_one_kg_vegetables[5]) 
broccoli = collectProduce(product_type_vegetables[6],produce_lifetime_days_vegetables[6],price_per_one_kg_vegetables[6])
brussel_sprouts = collectProduce(product_type_vegetables[7],produce_lifetime_days_vegetables[7],price_per_one_kg_vegetables[7])
cabbage = collectProduce(product_type_vegetables[8],produce_lifetime_days_vegetables[8],price_per_one_kg_vegetables[8])
carrots = collectProduce(product_type_vegetables[9],produce_lifetime_days_vegetables[9],price_per_one_kg_vegetables[9])
cauliflower = collectProduce(product_type_vegetables[10],produce_lifetime_days_vegetables[10],price_per_one_kg_vegetables[10])
celery = collectProduce(product_type_vegetables[11],produce_lifetime_days_vegetables[11],price_per_one_kg_vegetables[11])
cucumber = collectProduce(product_type_vegetables[12],produce_lifetime_days_vegetables[12],price_per_one_kg_vegetables[12])
kale = collectProduce(product_type_vegetables[13],produce_lifetime_days_vegetables[13],price_per_one_kg_vegetables[13])
lettuce = collectProduce(product_type_vegetables[14],produce_lifetime_days_vegetables[14],price_per_one_kg_vegetables[14])
onion = collectProduce(product_type_vegetables[15],produce_lifetime_days_vegetables[15],price_per_one_kg_vegetables[15])
parsnip = collectProduce(product_type_vegetables[16],produce_lifetime_days_vegetables[16],price_per_one_kg_vegetables[16])
potato = collectProduce(product_type_vegetables[17],produce_lifetime_days_vegetables[17],price_per_one_kg_vegetables[17])
spinach = collectProduce(product_type_vegetables[18],produce_lifetime_days_vegetables[18],price_per_one_kg_vegetables[18])
tomato = collectProduce(product_type_vegetables[19],produce_lifetime_days_vegetables[19],price_per_one_kg_vegetables[19])

#total overhead cost subtracted from the total cost of 60,000 kg of vegetables.
artichoke_min_overhead = getProducePriceMinOverhead(wheat, total_kg)
asparagus_min_overhead = getProducePriceMinOverhead(asparagus, total_kg)
garlic_min_overhead = getProducePriceMinOverhead(garlic, total_kg)
green_beans_min_overhead = getProducePriceMinOverhead(green_beans, total_kg)
beets_min_overhead = getProducePriceMinOverhead(beets, total_kg)
bell_peppers_min_overhead = getProducePriceMinOverhead(bell_peppers, total_kg)
broccoli_min_overhead = getProducePriceMinOverhead(broccoli, total_kg)
brussel_sprouts_min_overhead = getProducePriceMinOverhead(brussel_sprouts, total_kg)
cabbage_min_overhead = getProducePriceMinOverhead(cabbage, total_kg)
carrots_min_overhead = getProducePriceMinOverhead(carrots, total_kg)
cauliflower_min_overhead = getProducePriceMinOverhead(cauliflower, total_kg)
celery_min_overhead = getProducePriceMinOverhead(celery, total_kg)
cucumber_min_overhead = getProducePriceMinOverhead(cucumber, total_kg)
kale_min_overhead = getProducePriceMinOverhead(kale, total_kg)
lettuce_min_overhead = getProducePriceMinOverhead(lettuce, total_kg)
onion_min_overhead = getProducePriceMinOverhead(onion, total_kg)
parsnip_min_overhead = getProducePriceMinOverhead(parsnip, total_kg)
potato_min_overhead = getProducePriceMinOverhead(potato, total_kg)
spinach_min_overhead = getProducePriceMinOverhead(spinach, total_kg)
tomato_min_overhead = getProducePriceMinOverhead(tomato, total_kg)

#adjusted cost per unit of 60,000 kg of produce after subtracting overhead.
adj_artichoke = artichoke_min_overhead / total_kg
adj_asparagus = asparagus_min_overhead / total_kg
adj_garlic = garlic_min_overhead / total_kg
adj_green_beans = green_beans_min_overhead / total_kg
adj_beets = beets_min_overhead / total_kg
adj_bell_peppers = bell_peppers_min_overhead / total_kg
adj_broccoli = broccoli_min_overhead / total_kg
adj_brussel_sprouts = brussel_sprouts_min_overhead / total_kg
adj_cabbage = cabbage_min_overhead / total_kg
adj_carrots = carrots_min_overhead / total_kg
adj_cauliflower = cauliflower_min_overhead / total_kg
adj_celery = celery_min_overhead / total_kg
adj_cucumber = cucumber_min_overhead / total_kg 
adj_kale = kale_min_overhead / total_kg
adj_lettuce = lettuce_min_overhead / total_kg
adj_onion = onion_min_overhead / total_kg
adj_parsnip = parsnip_min_overhead / total_kg
adj_potato = potato_min_overhead / total_kg
adj_spinach = spinach_min_overhead / total_kg
adj_tomato = tomato_min_overhead / total_kg

#adjusted_beef = beef - total




#note: personnel get paid 1K CAD and 2.6 kg of free produce of their choice per month with this current process

