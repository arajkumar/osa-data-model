mgmt = graph.openManagement();

// for dependency version
service_version = mgmt.getPropertyKey('vertex_label');
if(service_version == null) {
    service_version = mgmt.makePropertyKey('vertex_label').dataType(String.class).make();
}

List<String> allKeys = [
        'vertex_label'
]

allKeys.each { k ->
    keyRef = mgmt.getPropertyKey(k);
    index_key = 'index_prop_key_'+k;
    if(null == mgmt.getGraphIndex(index_key)) {
        // For now, only build the simple single property index.
        mgmt.buildIndex(index_key, Vertex.class).addKey(keyRef).buildCompositeIndex()
    }
}
