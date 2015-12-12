# Machine generated - see build_spice.py

from numpy import array

inertial_frames = [
    ('J2000', [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, -0.0, 1.0]]),
    ('B1950',
     [[0.99992570795236291, 0.011178938126427691, 0.0048590038414544293],
      [-0.011178938137770135, 0.9999375133499887, -2.715792625851078e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('FK4',
     [[0.99992567949568767, 0.011181483239171792, 0.0048590037723143858],
      [-0.01118148322046629, 0.99993748489331347, -2.7170293744002029e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-118',
     [[0.99992567914061581, 0.011181514992482714, 0.0048590037714515821],
      [-0.011181514973402329, 0.99993748453824161, -2.7170448043105616e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-96',
     [[0.99992568569166396, 0.011180929131774816, 0.004859003787369841],
      [-0.011180929119611181, 0.99993749108928975, -2.7167601165747207e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-102',
     [[0.99992570058677066, 0.011179596947047826, 0.004859003823560055],
      [-0.011179596950612145, 0.99993750598439646, -2.716112767048625e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-108',
     [[0.99992568207060584, 0.011181252967069354, 0.0048590037785712081],
      [-0.011181252951082478, 0.99993748746823163, -2.7169174781036253e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-111',
     [[0.99992567608045124, 0.011181788652696216, 0.0048590037640154644],
      [-0.011181788630384961, 0.99993748147807704, -2.7171777842249146e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-114',
     [[0.99992567798323728, 0.011181618493732738, 0.004859003768639205],
      [-0.011181618473430402, 0.99993748338086308, -2.7170950987511777e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-122',
     [[0.99992567913790542, 0.011181515234874401, 0.0048590037714449962],
      [-0.011181515215791154, 0.99993748453553122, -2.7170449220961369e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-125',
     [[0.99992567676350608, 0.011181727569991416, 0.0048590037656752851],
      [-0.011181727548401311, 0.99993748216113176, -2.7171481022599927e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('DE-130',
     [[0.99992567951195044, 0.011181481784821675, 0.0048590037723539028],
      [-0.011181481766133343, 0.99993748490957624, -2.7170286676867509e-05],
      [-0.0048590038153592712, -2.7162594714247048e-05, 0.9999881946023742]]),
    ('GALACTIC',
     [[-0.054875539395742523, -0.87343710472759606, -0.48383499177002515],
      [0.49410945362774389, -0.44482959429757496, 0.74698224869989183],
      [-0.86766613568337381, -0.19807638961301985, 0.45598379452141991]]),
    ('DE-200', [[1.0, 0.0, -0.0], [-0.0, 1.0, -0.0], [-0.0, -0.0, 1.0]]),
    ('DE-202', [[1.0, 0.0, -0.0], [-0.0, 1.0, -0.0], [-0.0, -0.0, 1.0]]),
    ('MARSIAU',
     [[0.67325774746002498, 0.73940787491414595, -3.6947768825436786e-17],
      [-0.58963083782625325, 0.53688031082163401, 0.60340285625473833],
      [0.44616082366044196, -0.40624564781301037, 0.79743651350036859]]),
    ('ECLIPJ2000',
     [[1.0, 0.0, 0.0],
      [0.0, 0.91748206206918181, 0.39777715593191371],
      [0.0, -0.39777715593191371, 0.91748206206918181]]),
    ('ECLIPB1950',
     [[0.99992570795236291, 0.011178938126427691, 0.0048590038414544293],
      [-0.012189277138214926, 0.91736881787898283, 0.39785157220522011],
      [-9.9405009203520217e-06, -0.3978812427417045, 0.91743692784599817]]),
    ('DE-140',
     [[0.99992567653846676, 0.011181770119802481, 0.0048589521583800562],
      [-0.011181770179728694, 0.99993748168487007, -2.7154519585747306e-05],
      [-0.0048589520204735384, -2.7179184981447069e-05, 0.99998819485359658]]),
    ('DE-142',
     [[0.99992567654026054, 0.011181769732063588, 0.0048589526815459912],
      [-0.011181769790785997, 0.99993748168921248, -2.7154769316986656e-05],
      [-0.0048589525464097748, -2.7178939228786992e-05, 0.99998819485104773]]),
    ('DE-143',
     [[0.999925676543585, 0.011181774307743055, 0.0048589414674685858],
      [-0.011181774330053015, 0.99993748163825025, -2.7162211525057475e-05],
      [-0.0048589414161271738, -2.7171394236557294e-05, 0.99998819490533486]]),
    ]

inertial_frames = dict((key, array(value)) for key, value in inertial_frames)