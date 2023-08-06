from pdf import TransPDF


def print_hi():
    pdf = TransPDF(
        logo="logo-transporeon.png",
        image_path='https://truck-static.s3.eu-central-1.amazonaws.com/static/pdf'
    )

    pdf.set_default_font('bold', 14, '#001A26')
    pdf.add_text(28, 270.92, 'Coverage of this report')

    data = (
        {'vehicle': 'Vehicle 1', 'total_distance': '34569023495390425734578934257893425879342789534280957342085734257328593247890', 'average_weight': 50},
        {'vehicle': 'Vehicle 2', 'total_distance': 13.3, 'average_weight': 40},
        {'vehicle': 'Vehicle 3', 'total_distance': 22.1, 'average_weight': 40},
    )

    pdf.create_table({
        'template': 'default',
        'header': (
            {'title': 'Vehicle\nVehicle', 'width': 20},
            {'title': 'Total Distance (km)', 'width': 20},
            {'title': 'Average Weight (t)', 'width': 10},
        ),
        'data': [
            (
                item.get('vehicle'),
                item.get('total_distance'),
                item.get('average_weight')
            ) for item in data
        ],
        'footer': (
            'Total',
            55.7,
            120
        )
    })

    pdf.set_default_font('regular', 12, '#323232')
    file = open("test.pdf", "wb")
    file.write(pdf.raw().read())
    file.close()


if __name__ == '__main__':
    print_hi()

