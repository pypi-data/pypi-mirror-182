import math


class VH:
    """
    V and H coordinate math class.

    Warning: V and H coordinate systems may use at least two different
    algorithms, and are a kludge to allow integer based location
    markers.  If you can use a different geocoding system, you should.

    A quite horifying map of V&H's limit and skew can be found here:
        https://web.archive.org/web/20100430211425/http://www.trainfo.com/products_services/tra/vhpage.html
    at least as of 2010-11-02.

    This code is adapted from multiple sources.  Information about
    various algorythms can be found at the follow web addresses (as of
    2010-11-02):

        http://snippets.dzone.com/tag/latitude
        http://www.voip-info.org/wiki/view/V+and+H+Coordinates
        http://cpansearch.perl.org/src/JFREEMAN/Geo-Coordinates-VandH-XS-0.01/XS.xs

    Functions which demand a v,h (or lat,lon) pair can be called with
    either two integers or a tupple, as in
        print vh.distance(7000, 3000)
    or
        print vh.distance(vh.ll2vh(36.825492819825783, -88.207244148055793))

    """

    def __init__(self, v, h=None):
        if h is None:
            h = v[1]
            v = v[0]

        self.v = v
        self.h = h

        #
        # Set up constants
        #
        self.TRANSV = 6363.235
        self.TRANSH = 2250.700

        self.EX = 0.40426992
        self.EY = 0.68210848
        self.EZ = 0.60933887

        self.WX = 0.65517646
        self.WY = 0.37733790
        self.WZ = 0.65449210

        self.PX = -0.555977821730048699
        self.PY = -0.345728488161089920
        self.PZ = 0.755883902605524030

        self.RADIUS = 12481.103

        rot = math.radians(76.597497064)
        self.ROTC = math.cos(rot)
        self.ROTS = math.sin(rot)

        self.GX = 0.216507961908834992
        self.GY = -0.134633014879368199

        self.A = 0.151646645621077297

        self.Q = -0.294355056616412800
        self.Q2 = 0.0866448993556515751
        self.EPSILON = 0.0000001

        self.K1 = 0.99435487
        self.K2 = 0.00336523
        self.K3 = -0.00065596
        self.K4 = 0.00005606
        self.K5 = -0.00000188

        self.M_PI_2 = math.pi / 2.0

        self.K9 = self.RADIUS * self.ROTC
        self.K10 = self.RADIUS * self.ROTS

    def distance(self, v2, h2=None):
        """Calculate the distance (in miles) between the object's point and a second,
        supplied point (v2, h2)"""

        if h2 is None:
            h2 = v2[1]
            v2 = v2[0]

        v1 = self.v
        h1 = self.h

        # min_list = (0,41,121,361)                     # Known
        min_list = (0, 41, 121, 361, 1081, 3241, 9721, 29161)  # Surmised

        one_third = 1 / 3

        hd = abs(h1 - h2) / 3.0
        vd = abs(v1 - v2) / 3.0

        ivd = round(vd)
        ihd = round(hd)

        sum = (ivd**2) + (ihd**2)

        n = 1

        while sum > 1777:
            ivd = float(round(ivd / 3))
            ihd = float(round(ihd / 3))
            sum = ivd**2 + ihd**2
            n = n + 1

        mult = 9**n / 10.0

        sum = sum * mult

        z_bs = math.sqrt(sum)

        if z_bs < min_list[n - 1]:
            z_bs = min_list[n - 1]

        return z_bs

    def vh2ll(self):
        """Convert a V&H coordinate to a latitude and longitude value pair"""

        v = self.v
        h = self.h

        t1 = (v - self.TRANSV) / self.RADIUS
        t2 = (h - self.TRANSH) / self.RADIUS
        vhat = self.ROTC * t2 - self.ROTS * t1
        hhat = self.ROTS * t2 + self.ROTC * t1

        e = math.cos(math.sqrt(vhat**2 + hhat**2))
        w = math.cos(math.sqrt(vhat**2 + (hhat - 0.4) * (hhat - 0.4)))
        fx = self.EY * w - self.WY * e
        fy = self.EX * w - self.WX * e
        b = fx * self.GX + fy * self.GY
        c = fx * fx + fy * fy - self.Q2
        disc = b * b - self.A * c

        if abs(disc) < self.EPSILON:
            z = b / self.A
            x = (self.GX * z - fx) / self.Q
            y = (fy - self.GY * z) / self.Q
        else:
            delta = math.sqrt(disc)
            z = (b + delta) / self.A
            x = (self.GX * z - fx) / self.Q
            y = (fy - self.GY * z) / self.Q
            if vhat * (self.PX * x + self.PY * y + self.PZ * z) < 0:  # wrong direction
                z = (b - delta) / self.A
                x = (self.GX * z - fx) / self.Q
                y = (fy - self.GY * z) / self.Q

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
                + lat2
                * (bi[2] + lat2 * (bi[3] + lat2 * (bi[4] + lat2 * (bi[5] + lat2 * (bi[6])))))
            )
        )
        earthlat = math.degrees(earthlat)

        #
        #      Adjust longitude by 52 degrees:
        #
        lon = math.degrees(math.atan2(x, y))
        earthlon = lon + 52.0

        result = (earthlat, -earthlon)
        return result

    def ll2vh(self, lat, lon=None):

        if lon is None:
            lon = lat[1]
            lat = lat[0]

        lat = math.radians(lat)
        lon = math.radians(lon)

        lon1 = lon + math.radians(52.0)

        latsq = lat * lat
        lat1 = lat * (
            self.K1 + (self.K2 + (self.K3 + (self.K4 + self.K5 * latsq) * latsq) * latsq) * latsq
        )

        cos_lat1 = math.cos(lat1)
        x = cos_lat1 * math.sin(-lon1)
        y = cos_lat1 * math.cos(-lon1)
        z = math.sin(lat1)
        e = self.EX * x + self.EY * y + self.EZ * z
        w = self.WX * x + self.WY * y + self.WZ * z
        if e > 1.0:
            e = 1.0
        if w > 1.0:
            w = 1.0
        e = self.M_PI_2 - math.atan(e / math.sqrt(1 - e**2))
        w = self.M_PI_2 - math.atan(w / math.sqrt(1 - w**2))
        ht = (e * e - w * w + 0.16) / 0.8
        vt = math.sqrt(abs(e * e - ht * ht))
        if (self.PX * x + self.PY * y + self.PZ * z) < 0:
            vt = -vt
        v = self.TRANSV + self.K9 * ht - self.K10 * vt
        h = self.TRANSH + self.K10 * ht + self.K9 * vt
        return (v, h)

    def km2miles(self, kilometers):
        return kilometers * 0.621371192237

    def miles2km(self, miles):
        return miles * 1.609344

    def distance_algorithm2(self, v2, h2=None):
        """Calculate the distance (in miles) between the object's
        point and a second, supplied point (v2, h2) -- uses the
        shorter algorithm."""

        if h2 is None:
            h2 = v2[1]
            v2 = v2[0]

        v1 = self.v
        h1 = self.h

        z = math.sqrt((h1 - h2) ** 2 + (v1 - v2) ** 2) * 0.316225224

        return z
