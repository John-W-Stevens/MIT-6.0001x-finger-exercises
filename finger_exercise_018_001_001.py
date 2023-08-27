# Figure 18.5 code

def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances - pylab.array(distances)
    forces = pylab.array(masses)*9.81
    pylab.plot(forces, distances, 'ko', label = 'Measured displacements')
    pylab.title('Measured Displacements of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')
    #find linear fit
    a,b = pylab.polyfit(forces, distances, 1)
    predictedDistances = a*pylab.array(forces) + b
    k = 1.0/a #see explanation in text
    pylab.plot(forces, predictedDistances, label = 'Displacements predicted by \nlinear fit, k =' + str(round(k, 5)))
    pylab.legend(loc = 'best')

# Modify the code in Figure 18.5 (above) so that it produces the plot in Figure 18.8 (see textbook)