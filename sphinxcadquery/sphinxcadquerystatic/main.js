if ( WEBGL.isWebGLAvailable() === false ) {

    document.body.appendChild( WEBGL.getWebGLErrorMessage() );

}

var scenes = [], views, t, canvas, renderer;
var render_queued_flag = false;

window.addEventListener('load', init, false);
window.addEventListener('scroll', queueRender, false);

function queueRender() {

    if ( !render_queued_flag ) {

        render_queued_flag = true;
        requestAnimationFrame( render );

    }

}

function load_amf_into_scene( scene ) {

    return function ( amfobject ) {

        scene.add( amfobject );
        queueRender();

    }

}

function load_stl_into_scene( scene ) {

    return function ( geometry ) {

        var material = new THREE.MeshPhongMaterial( {

            color: scene.userData.view.color,
            specular: 0x111111,
            shininess: 100,

        } );
        var mesh = new THREE.Mesh( geometry, material );
        mesh.castShadow = true;
        mesh.receiveShadow = true;
        scene.add( mesh );
        queueRender();

    }

}

function init() {

    var canvasElement = document.createElement('canvas');
    canvasElement.id = 'sphinxcadquerycanvas';
    document.body.appendChild(canvasElement);

    canvas = document.getElementById( 'sphinxcadquerycanvas' );

    renderer = new THREE.WebGLRenderer( { canvas: canvas, antialias: true } );
    renderer.setPixelRatio( window.devicePixelRatio );

    views = document.querySelectorAll( '.sphinxcadqueryview' );

    for ( var n = 0; n < views.length; n ++ ) {

        var scene = new THREE.Scene();
        scene.background = new THREE.Color( 0xffffff );

        scene.userData.view = views[ n ];

        var loader = new THREE.STLLoader();
        loader.load( scene.userData.view.fname, load_stl_into_scene( scene ) );

        scene.add( new THREE.AmbientLight( 0x888888 ) );

        var grid = new THREE.GridHelper( 50, 50, 0x555555, 0xbbbbbb );
        grid.rotateOnAxis( new THREE.Vector3( 1, 0, 0 ), 90 * ( Math.PI / 180 ) );
        scene.add( grid );

        var camera = new THREE.PerspectiveCamera( 30, 1, 1, 10000 );
        camera.up.set( 0, 0, 1 );
        camera.position.set( 0, - 9, 6 );
        camera.add( new THREE.PointLight( 0xffffff, 0.6 ) );
        scene.add( camera );
        scene.userData.camera = camera;

        var controls = new THREE.OrbitControls( camera, views[ n ] );
        controls.addEventListener( 'change', queueRender );
        scene.userData.controls = controls;

        scenes.push( scene );

    }

    t = 0;
    queueRender();

}

function updateSize() {

    var width = canvas.clientWidth;
    var height = canvas.clientHeight;

    if ( canvas.width !== width || canvas.height !== height ) {

        renderer.setSize( width, height, false );

    }

}

function render() {

    updateSize();

    renderer.setClearColor( 0xffffff );
    renderer.setScissorTest( false );
    renderer.clear();

    renderer.setClearColor( 0x000000 );
    renderer.setScissorTest( true );

    scenes.forEach( function ( scene ) {

        var rect = scene.userData.view.getBoundingClientRect();
        // check if it's offscreen. If so skip it
        if ( rect.bottom < 0 || rect.top > renderer.domElement.clientHeight ||
             rect.right < 0 || rect.left > renderer.domElement.clientWidth ) {

            return; // it's off screen

        }

        // set the viewport
        var width = rect.right - rect.left;
        var height = rect.bottom - rect.top;
        var left = rect.left;
        var bottom = renderer.domElement.clientHeight - rect.bottom;

        renderer.setViewport( left, bottom, width, height );
        renderer.setScissor( left, bottom, width, height );

        renderer.render( scene, scene.userData.camera );

    } );

    t ++;
    render_queued_flag = false;

}
