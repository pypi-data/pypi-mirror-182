import graphviz
import os
from importlib.resources import path

aws_icon_prefix = 'Arch_Amazon-'
aws_icon_suffix = '_64.png'
aws_icon_location = 'resource/'

resources = [
    {
        "arn": "arn1",
        "label": "ec2"
    },
    {
        "arn": "arn2",
        "label": "ec2"
    },
    {
        "arn": "rds",
        "label": "rds"
    },
    {
        "arn": "alb",
        "label": "elasticloadbalancing"
    }
]
links = [
    {
        "from": "arn1",
        "to": "rds"
    },
    {
        "from": "arn2",
        "to": "rds"
    },
    {
        "from": "alb",
        "to": "arn1"
    },
    {
        "from": "alb",
        "to": "arn2"
    }
]


def get_icon_location(component, image=0):
    location = ''
    image_name = aws_icon_prefix + component.upper() + aws_icon_suffix
    #os.chdir(aws_icon_location)
    #files = os.listdir(aws_icon_location)
    #for root, dirs, files in os.walk(aws_icon_location):
    #    print("root", root)
    
    with path('archreactorpy', 'resource') as images_path:
        images = os.listdir(images_path)
        print("images", images)

        #files = os.path.join(images_path, images)
        #return_code = subprocess.call(['afplay', audio_file])
        for image in images:
            print("name", image)
            print("image_name", image_name)
            if image.__eq__(image_name):
                location = aws_icon_location + image
                print(location)
                break
    return location


def create_graph(nodes, edges, name):
    print('architecture diagram creation under process...')
    g = graphviz.Graph()
    for node in nodes:
        print('node of label', node['label'])
        image_location = "./resource/icons/Arch_Amazon-EC2_64.png"  
        #get_icon_location(node['label'])
        g.node(name = node['arn'], label = node['label'], shape = "plaintext", image = image_location)
    for edge in edges:
        g.edge(edge['from'], edge['to'])
    g.render(name)
    print('processing completed successfully!!!')

# main function
def main():
    # name of the graph ({product}-{env}-architecture-diagram)
    example_name = 'profilex-qa-architecture-diagram'
    create_graph(resources, links, example_name)

main()
