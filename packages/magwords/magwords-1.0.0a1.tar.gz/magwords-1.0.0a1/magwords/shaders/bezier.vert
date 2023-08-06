#version 460

layout (location = 0) in vec2 position;
layout (location = 1) in mat3 model;
layout (location = 0) out vec2 outAttrib;

layout (std140, binding = 0) uniform Env {
    vec2 inch_per_dot;
    vec2 window;
};

const vec2[] attrib = vec2[3] (
    vec2(0, 0),
    vec2(0.5, 0),
    vec2(1, 1)
);

const float inch_per_point = 1.0 / 72.0;

void main() {
    vec2 window_inch = window * inch_per_dot;
    mat3 proj = mat3(
        window.y / window.x, 0, 0,
        0, 1, 0,
        0, 0, 1
    );
    vec3 p = vec3(inch_per_point / window_inch * 2, 1) * (model * vec3(position, 1));
    p = proj * vec3(p.xy, 1);
    gl_Position = vec4(p.xy, 0, 1);
    outAttrib = attrib[gl_VertexID % 3];
}