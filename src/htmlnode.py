

class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        pass

    def props_to_html(self):
        if self.props is None:
            return ''
        if not isinstance(self.props, dict):
            return ''
        return ' '.join(['='.join([k,'"'+v+'"']) for [k,v] in self.props.items()])

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag=None,value=None,props=None):
        super().__init__(tag=tag,value=value,props=props)
        self.children = None
        
    def to_html(self):
        if self.value:
            if not self.tag:
                return self.value
            
            if self.props:
                
                return "<"+self.tag+" "+self.props_to_html()+">"+self.value+"</"+self.tag+">"

            return "<"+self.tag+">"+self.value+"</"+self.tag+">"
            
        raise ValueError('All leaf nodes must have a value')




class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag,children=children,props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        
        if not self.children:
            raise ValueError("All parent nodes must have children")
        
        full_html = f'<{self.tag}>'
        
        if isinstance(self.children,list):
            if len(self.children) == 0:
                raise ValueError("All parent nodes must have children")
            
            for node in self.children:
                if isinstance(node, LeafNode) or isinstance(node, ParentNode):
                    full_html += node.to_html()
                else:
                    raise ValueError("Children must be either LeafNode or ParentNode")
                
            return full_html + f'</{self.tag}>'

        raise ValueError("Children must be a list of LeafNode or ParentNode")

            
            
                
                