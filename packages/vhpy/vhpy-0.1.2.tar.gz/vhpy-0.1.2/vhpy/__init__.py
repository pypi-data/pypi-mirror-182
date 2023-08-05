import math

from . import constants

__version__ = "0.1.2"


def get_lat_long(v: float, h: float) -> (float, float):
    """Convert a V&H coordinate to a latitude and longitude value pair"""
    t1 = (v - constants.TRANSV) / constants.RADIUS
    t2 = (h - constants.TRANSH) / constants.RADIUS
    vhat = constants.ROTC * t2 - constants.ROTS * t1
    hhat = constants.ROTS * t2 + constants.ROTC * t1

    e = math.cos(math.sqrt(vhat**2 + hhat**2))
    w = math.cos(math.sqrt(vhat**2 + (hhat - 0.4) * (hhat - 0.4)))
    fx = constants.EY * w - constants.WY * e
    fy = constants.EX * w - constants.WX * e
    b = fx * constants.GX + fy * constants.GY
    c = fx * fx + fy * fy - constants.Q2
    disc = b * b - constants.A * c

    if abs(disc) < constants.EPSILON:
        z = b / constants.A
        x = (constants.GX * z - fx) / constants.Q
        y = (fy - constants.GY * z) / constants.Q
    else:
        delta = math.sqrt(disc)
        z = (b + delta) / constants.A
        x = (constants.GX * z - fx) / constants.Q
        y = (fy - constants.GY * z) / constants.Q
        if vhat * (constants.PX * x + constants.PY * y + constants.PZ * z) < 0:  # wrong direction
            z = (b - delta) / constants.A
            x = (constants.GX * z - fx) / constants.Q
            y = (fy - constants.GY * z) / constants.Q

    lat = math.asin(z)

    bi = (
        1.00567724920722457,
        -0.00344230425560210245,
        0.000713971534527667990,
        -0.0000777240053499279217,
        0.00000673180367053244284,
        -0.000000742595338885741395,
        0.0000000905058919926194134,
    )
    lat2 = lat * lat

    earthlat = lat * (
        bi[0]
        + lat2
        * (
            bi[1]
            + lat2 * (bi[2] + lat2 * (bi[3] + lat2 * (bi[4] + lat2 * (bi[5] + lat2 * (bi[6])))))
        )
    )
    earthlat = math.degrees(earthlat)

    # Adjust longitude by 52 degrees
    lon = math.degrees(math.atan2(x, y))
    earthlon = lon + 52.0

    result = (earthlat, -earthlon)
    return result
