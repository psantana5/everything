class Circle {
private:
    double radius;

public:
    void setRadius(double r) {
        radius = r;
    }

    double getArea() {
        return 3.14 * radius * radius;
    }
};

int main() {
    Circle c;
    c.setRadius(5.0);
    double area = c.getArea();
    cout << "Area: " << area << endl;
    return 0;
}
