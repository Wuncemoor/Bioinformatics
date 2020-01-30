def mating_phenotype(dominant, hetero, recessive):
    total_population = dominant + hetero + recessive
    
    #first probability
    dom_chance = (dominant/total_population)
    het_chance = (hetero/total_population)
    rec_chance = (recessive/total_population)
    
    #Chance of offspring w/ phenotype
    domdom, domhet, domrec, hetdom, hethet, hetrec, recdom, rechet, recrec = 1, 1, 1, 1, 0.75, 0.5, 1, 0.5, 0
    
    #first + second probabilities, non-replacing, w/ applied offpsring probabilities
    domdom_chance = (dom_chance * ((dominant-1)/(total_population-1)))*domdom
    domhet_chance = (dom_chance * ((hetero)/(total_population-1)))*domhet
    domrec_chance = (dom_chance * ((recessive)/(total_population-1)))*domrec
    hetdom_chance = (het_chance * ((dominant)/(total_population-1)))*hetdom
    hethet_chance = (het_chance * ((hetero-1)/(total_population-1)))*hethet
    hetrec_chance = (het_chance * ((recessive)/(total_population-1)))*hetrec
    recdom_chance = (rec_chance * ((dominant)/(total_population-1)))*recdom
    rechet_chance = (rec_chance * ((hetero)/(total_population-1)))*rechet
    recrec_chance = (rec_chance * ((recessive-1)/(total_population-1)))*recrec
    
    
    return domdom_chance + domhet_chance + domrec_chance + hetdom_chance + hethet_chance + hetrec_chance + recdom_chance + rechet_chance + recrec_chance
    

    