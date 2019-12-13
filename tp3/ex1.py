from pyDatalog import  pyDatalog

pyDatalog.create_terms('fritz,X,croakes,eatFlies,frog,chirps,sings,canary,green,yellow')
#pyDatalog.create_atoms('croakes','eatFlies','frog','chirps','sings','canary','green','yellow')

frog(X) <= croakes(X) & eatFlies(X)
canary(X) <= sings(X) & chirps(X)

#frog(X) <= green(X)
green(X) <= frog(X)
canary(X) <= yellow(X)

# fritz is a frog
#+ (frog(fritz))

pyDatalog.assert_fact('croakes','fritz')
pyDatalog.assert_fact('eatFlies','fritz')

print("Frog :",pyDatalog.ask('frog(X)').answers)
print("Green :",pyDatalog.ask('green(X)').answers)