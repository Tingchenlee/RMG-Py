
database(
    thermoLibraries=['surfaceThermoPt111', 'primaryThermoLibrary'],
    reactionLibraries = [], 
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['Surface_Adsorption_Abstraction_vdW'], # <<<<< ONLY ONE REACTION FAMILY
    kineticsEstimator = 'rate rules',

)

catalystProperties(
    bindingEnergies= {
                         'H':(-2.75367887E+00, 'eV/molecule'),
                         'C':(-7.02515507E+00, 'eV/molecule'),
                         'N':(-4.63224568E+00, 'eV/molecule'),
                         'O':(-3.81153179E+00, 'eV/molecule'),
                      },
    surfaceSiteDensity=(2.483E-09, 'mol/cm^2'),
)

species(
   label='N#N.[Pt]',
   reactive=True,
   structure=adjacencyList(
       """
1  N u0 p1 c0 {2,T}
2  N u0 p1 c0 {1,T}
3  X u0 p0 c0
"""),
)

species(
   label='[Pt]N=N',
   reactive=True,
   structure=adjacencyList(
       """
1  N u0 p1 c0 {2,D} {4,S}
2  N u0 p1 c0 {1,D} {3,S}
3  H u0 p0 c0 {2,S}
4  X u0 p0 c0 {1,S}
"""),
)


species(
    label='N2',
    reactive=False,
    structure=SMILES("N#N"),
)

species(
    label='vacantX',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)
#----------
# Reaction systems
surfaceReactor(
    temperature=(800,'K'),
    initialPressure=(1.0, 'bar'),
    initialGasMoleFractions={
        "N2": 1.0,
    },
    initialSurfaceCoverages={
        "vacantX": 0.5,
        "N#N.[Pt]": 0.25,
        "[Pt]N=N": 0.25
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    terminationTime=(0.1, 's'),
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=1e-5,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000,
)

options(
    units='si',
    generateOutputHTML=True,
    generatePlots=False,
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)
