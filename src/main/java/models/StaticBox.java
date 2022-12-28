package models;

import models.Box;

public class StaticBox extends Box {
    double x;
    double y;
    double z;
    double coor_x;
    double coor_y;
    double coor_z;
    double density;

    public StaticBox(double x, double y, double z, double density, double coor_x, double coor_y, double coor_z) {
        super(x, y, z, density);
        this.coor_x = coor_x;
        this.coor_y = coor_y;
        this.coor_z = coor_z;
    }

}
