const std = @import("std");
const rl = @import("raylib");

const Text = @import("text.zig").Text;
const Vector2 = @import("vector2.zig").Vector2;
const TextArray = @import("text_array.zig").TextArray;
const EntityTrace = @import("trace.zig").EntityTrace;

const frame_memory = @import("../../frame_memory.zig");

pub const BlockType = enum(i32) {
    None = -1,

    // === Control Flow ===
    CONTROL = 1000,
    If, // bool
    ElseIf, // bool
    Else, // -
    Repeat, // bool
    While, // bool
    ForEach, // array
    ForEachPathArray, // path->array
    Continue, // -
    Break, // -

    // === Statements ===
    STATEMENT = 10000,
    ReturnSuccess, // none=bool
    ReturnFailed, // none=bool
    Log, // text=void
    ExecuteCommand, // text, []text=void

    SetValueInt, // text, blockvalue=void
    SetValueFloat, // text, blockvalue=void
    SetValueBool, // text, blockvalue=void
    SetValueText, // text, blockvalue=void
    SetValueVector2, // text, blockvalue=void

    DrSetText, // text, text=bool

    // === Literals ===
    REPORTER = 1000000,
    GetValueInt, // Integer constant value - text=i32
    GetValueFloat, // Floating point constant value - text=f32
    GetValueBool, // Boolean constant value (true/false) - text=bool
    GetValueText, // String constant value - text=text

    // === Variables & Data ===
    REPORTER_DR = 1001000,
    DrGetInt, // dr.getInt() - text=i32
    DrGetU8, // dr.getU8()
    DrGetU16, // dr.getU16()
    DrGetU32, // dr.getU32()
    DrGetFloat, // dr.getFloat()
    DrGetBool, // dr.getBool()
    DrGetText, // dr.getText()
    DrGetAny, // dr.getAny()
    DrGetAnyArray, // Get Any Array //TODO: How to use this generically?  Need a way to deal with it...

    // === Logic & Comparison ===
    REPORTER_LOGIC = 1002000,
    LogicAnd, // Logical AND: a && b - bool,bool=bool
    LogicOr, // Logical OR: a || b - bool,bool=bool
    LogicNot, // Logical NOT: !a - bool=bool
    LogicEqual, // Equality: a == b - float,float=bool
    LogicNotEqual, // Inequality: a != b - float,float=bool
    LogicLess, // Less than: a < b - float,float=bool
    LogicLessEqual, // Less than or equal: a <= b - float,float=bool
    LogicGreater, // Greater than: a > b - float,float=bool
    LogicGreaterEqual, // Greater than or equal: a >= b - float,float=bool

    // === Scalar Math - Basic ===
    REPORTER_MATH = 1003000,
    MathAdd, // Addition: a + b - float,float=float
    MathSub, // Subtraction: a - b - float,float=float
    MathMultiply, // Multiplication: a * b - float,float=float
    MathDivide, // Division: a / b - float,float=float
    MathModulus, // Modulo: a % b, remainder after division - float,float=float
    MathPower, // Power: a^b, exponentiation - float,int=float
    MathSquareRoot, // Square root: √x - float=float
    MathAbs, // Absolute value: |x|  - float=float
    MathSign, // Sign of x: returns -1, 0, or 1  - float,float=float

    // === Scalar Math - Rounding ===
    MathFloor, // Round down to integer - float=float
    MathCeil, // Round up to integer - float=float
    MathRound, // Round to nearest integer - float=float

    // === Scalar Math - Range ===
    MathMin, // Minimum of two values - float,float=float
    MathMax, // Maximum of two values - float,float=float
    MathClamp, // Constrain value between min and max - float,float=float

    // === Scalar Math - Interpolation ===
    MathLerp, // Linear interpolation: a + (b-a)*t - float,float,float=float
    MathSmoothStep, // Smooth hermite interpolation between edges - - float,float=float
    MathStep, // Step function: returns 0 if x < edge, else 1 - - float,float=float
    MathSaturate, // Clamp value to [0, 1] range - float,float=float

    // === Scalar Math - Trigonometry ===
    MathSin, // Sine function - float=float
    MathCos, // Cosine function  - float=float
    MathTan, // Tangent function  - float=float
    MathAtan2, // Two-argument arctangent: angle from x-axis to point (y,x)  - float=float

    // === Randomness ===
    MathRandom, // Random value in range [0, 1] - -=float
    MathRandomRange, // Random value in range [min, max] - float,float=float

    // === Vector2 Construction ===
    MathVec2, // Construct vec2 from (x, y) - float,float -- Vector2
    MathVec2X, // Extract x component from vec2 - vec2=float
    MathVec2Y, // Extract y component from vec2 - vec2=float

    // === Vector2 Arithmetic ===
    MathVec2Add, // Vector addition: v1 + v2 - vec2,vec2=vec2
    MathVec2Sub, // Vector subtraction: v1 - v2 - vec2,vec2=vec2
    MathVec2Mul, // Component-wise multiply: (v1.x*v2.x, v1.y*v2.y) - vec2,vec2=vec2
    MathVec2Div, // Component-wise divide: (v1.x/v2.x, v1.y/v2.y) - vec2,vec2=vec2
    MathVec2Scale, // Scalar multiply: v * scalar - vec2,float=vec2

    // === Vector2 Operations ===
    MathVec2Length, // Vector magnitude: |v|  - vec2=float
    MathVec2LengthSquare, // Squared length: |v|² (avoids sqrt for comparisons)  - vec2=float
    MathVec2Normalize, // Unit vector: v / |v|  - vec2=vec2
    MathVec2Distance, // Distance between points: |v1 - v2|  - vec2,vec2=vec2
    MathVec2Dot, // Dot product: v1.x*v2.x + v1.y*v2.y  - vec2,vec2=float
    MathVec2Angle, // Angle of vector from positive x-axis - vec2=float
    MathVec2Rotate, // Rotate vector by angle (radians) - vec2=float

    // // === Vector3 Construction ===
    // reporter_math_vec3, // Construct vec3 from (x, y, z)
    // reporter_math_vec3_splat, // Construct vec3 from single value: (x, x, x)
    // reporter_math_vec3_from_v2, // Construct vec3 from vec2 and z: (v2.x, v2.y, z)
    // reporter_math_vec3_x, // Extract x component from vec3
    // reporter_math_vec3_y, // Extract y component from vec3
    // reporter_math_vec3_z, // Extract z component from vec3

    // // === Vector3 Arithmetic ===
    // reporter_math_vec3_add, // Vector addition: v1 + v2
    // reporter_math_vec3_sub, // Vector subtraction: v1 - v2
    // reporter_math_vec3_mul, // Component-wise multiply: (v1.x*v2.x, v1.y*v2.y, v1.z*v2.z)
    // reporter_math_vec3_div, // Component-wise divide: (v1.x/v2.x, v1.y/v2.y, v1.z/v2.z)
    // reporter_math_vec3_scale, // Scalar multiply: v * scalar

    // // === Vector3 Operations ===
    // reporter_math_vec3_length, // Vector magnitude: |v|
    // reporter_math_vec3_length_sq, // Squared length: |v|² (avoids sqrt for comparisons)
    // reporter_math_vec3_normalize, // Unit vector: v / |v|
    // reporter_math_vec3_distance, // Distance between points: |v1 - v2|
    // reporter_math_vec3_dot, // Dot product: v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
    // reporter_math_vec3_cross, // Cross product: perpendicular vector to v1 and v2

    // // === Vector4 Construction ===
    // reporter_math_vec4, // Construct vec4 from (x, y, z, w)
    // reporter_math_vec4_splat, // Construct vec4 from single value: (x, x, x, x)
    // reporter_math_vec4_from_v3, // Construct vec4 from vec3 and w: (v3.x, v3.y, v3.z, w)
    // reporter_math_vec4_x, // Extract x (or r) component from vec4
    // reporter_math_vec4_y, // Extract y (or g) component from vec4
    // reporter_math_vec4_z, // Extract z (or b) component from vec4
    // reporter_math_vec4_w, // Extract w (or a) component from vec4

    // // === Vector4 Arithmetic ===
    // reporter_math_vec4_add, // Vector addition: v1 + v2
    // reporter_math_vec4_sub, // Vector subtraction: v1 - v2
    // reporter_math_vec4_mul, // Component-wise multiply: (v1.x*v2.x, v1.y*v2.y, v1.z*v2.z, v1.w*v2.w)
    // reporter_math_vec4_div, // Component-wise divide: (v1.x/v2.x, v1.y/v2.y, v1.z/v2.z, v1.w/v2.w)
    // reporter_math_vec4_scale, // Scalar multiply: v * scalar

    // // === Vector4 Operations ===
    // reporter_math_vec4_length, // Vector magnitude: |v|
    // reporter_math_vec4_length_sq, // Squared length: |v|² (avoids sqrt for comparisons)
    // reporter_math_vec4_normalize, // Unit vector: v / |v|
    // reporter_math_vec4_dot, // Dot product: v1.x*v2.x + v1.y*v2.y + v1.z*v2.z + v1.w*v2.w

    // // === Scalar Math - Shader Utilities ===
    // reporter_math_fract, // Fractional part: x - floor(x), returns [0, 1)
    // reporter_math_reflect, // Reflect incident vector across normal
    // reporter_math_refract, // Refract incident vector through surface with refractive index

    // === Special ===
    SPECIAL = 9000000,
    // special_return_success,
};

pub const In_V2_Out_Float = enum(i32) {
    MathVec2X, // Extract x component from vec2 - vec2=float
    MathVec2Y, // Extract y component from vec2 - vec2=float
    MathVec2Length, // Vector magnitude: |v|  - vec2=float
    MathVec2LengthSquare, // Squared length: |v|² (avoids sqrt for comparisons)  - vec2=float
    MathVec2Angle, // Angle of vector from positive x-axis - vec2=float
    MathVec2Rotate, // Rotate vector by angle (radians) - vec2=float
};

pub const In_V2_V2_Out_Float = enum(i32) {
    MathVec2Dot, // Dot product: v1.x*v2.x + v1.y*v2.y  - vec2,vec2=float
};

pub const In_V2_V2_Out_V2 = enum(i32) {
    MathVec2Add, // Vector addition: v1 + v2 - vec2,vec2=vec2
    MathVec2Sub, // Vector subtraction: v1 - v2 - vec2,vec2=vec2
    MathVec2Mul, // Component-wise multiply: (v1.x*v2.x, v1.y*v2.y) - vec2,vec2=vec2
    MathVec2Div, // Component-wise divide: (v1.x/v2.x, v1.y/v2.y) - vec2,vec2=vec2
    MathVec2Distance, // Distance between points: |v1 - v2|  - vec2,vec2=vec2
};

pub const In_V2_Out_V2 = enum(i32) {
    // === Vector2 Construction ===
    MathVec2, // Construct vec2 from (x, y) - float,float -- Vector2
    MathVec2X, // Extract x component from vec2 - vec2=float
    MathVec2Y, // Extract y component from vec2 - vec2=float

    // === Vector2 Arithmetic ===
    MathVec2Add, // Vector addition: v1 + v2 - vec2,vec2=vec2
    MathVec2Sub, // Vector subtraction: v1 - v2 - vec2,vec2=vec2
    MathVec2Mul, // Component-wise multiply: (v1.x*v2.x, v1.y*v2.y) - vec2,vec2=vec2
    MathVec2Div, // Component-wise divide: (v1.x/v2.x, v1.y/v2.y) - vec2,vec2=vec2
    MathVec2Scale, // Scalar multiply: v * scalar - vec2,float=vec2

    // === Vector2 Operations ===
    MathVec2Length, // Vector magnitude: |v|  - vec2=float
    MathVec2LengthSquare, // Squared length: |v|² (avoids sqrt for comparisons)  - vec2=float
    MathVec2Normalize, // Unit vector: v / |v|  - vec2=vec2
    MathVec2Distance, // Distance between points: |v1 - v2|  - vec2,vec2=vec2
    MathVec2Dot, // Dot product: v1.x*v2.x + v1.y*v2.y  - vec2,vec2=float
    MathVec2Angle, // Angle of vector from positive x-axis - vec2=float
    MathVec2Rotate, // Rotate vector by angle (radians) - vec2=float
};

pub const In_V2_Float_Out_V2 = enum(i32) {
    // === Vector2 Construction ===
    MathVec2, // Construct vec2 from (x, y) - float,float -- Vector2
    MathVec2X, // Extract x component from vec2 - vec2=float
    MathVec2Y, // Extract y component from vec2 - vec2=float

    // === Vector2 Arithmetic ===
    MathVec2Add, // Vector addition: v1 + v2 - vec2,vec2=vec2
    MathVec2Sub, // Vector subtraction: v1 - v2 - vec2,vec2=vec2
    MathVec2Mul, // Component-wise multiply: (v1.x*v2.x, v1.y*v2.y) - vec2,vec2=vec2
    MathVec2Div, // Component-wise divide: (v1.x/v2.x, v1.y/v2.y) - vec2,vec2=vec2
    MathVec2Scale, // Scalar multiply: v * scalar - vec2,float=vec2

    // === Vector2 Operations ===
    MathVec2Length, // Vector magnitude: |v|  - vec2=float
    MathVec2LengthSquare, // Squared length: |v|² (avoids sqrt for comparisons)  - vec2=float
    MathVec2Normalize, // Unit vector: v / |v|  - vec2=vec2
    MathVec2Distance, // Distance between points: |v1 - v2|  - vec2,vec2=vec2
    MathVec2Dot, // Dot product: v1.x*v2.x + v1.y*v2.y  - vec2,vec2=float
    MathVec2Angle, // Angle of vector from positive x-axis - vec2=float
    MathVec2Rotate, // Rotate vector by angle (radians) - vec2=float
};

pub const In_Float_Float_Out_V2 = enum(i32) {
    MathVec2,
};

pub const In_Out_Float = enum(i32) {
    MathRandom, // Random value in range [0, 1] - -=float
};

pub const In_Float_Out_Float = enum(i32) {
    MathSquareRoot, // Square root: √x - float=float
    MathAbs, // Absolute value: |x|  - float=float
    MathFloor, // Round down to integer - float=float
    MathCeil, // Round up to integer - float=float
    MathRound, // Round to nearest integer - float=float
    MathSin, // Sine function - float=float
    MathCos, // Cosine function  - float=float
    MathTan, // Tangent function  - float=float
};

pub const In_Float_Float_Out_Float = enum(i32) {
    MathAdd, // Addition: a + b - float,float=float
    MathSub, // Subtraction: a - b - float,float=float
    MathMultiply, // Multiplication: a * b - float,float=float
    MathDivide, // Division: a / b - float,float=float
    MathModulus, // Modulo: a % b, remainder after division - float,float=float
    MathSign, // Sign of x: returns -1, 0, or 1  - float,float=float
    MathMin, // Minimum of two values - float,float=float
    MathMax, // Maximum of two values - float,float=float
    MathClamp, // Constrain value between min and max - float,float=float
    MathSmoothStep, // Smooth hermite interpolation between edges - - float,float=float
    MathStep, // Step function: returns 0 if x < edge, else 1 - - float,float=float
    MathSaturate, // Clamp value to [0, 1] range - float,float=float
    MathRandomRange, // Random value in range [min, max] - float,float=float
};

pub const In_Float_Float_Float_Out_Float = enum(i32) {
    MathLerp, // Linear interpolation: a + (b-a)*t - float,float,float=float
};

pub const In_Float_Int_Out_Float = enum(i32) {
    MathPower, // Power: a^b, exponentiation - float,int=float
};

pub const In_Float_Float_Out_Bool = enum(i32) {
    LogicEqual, // Equality: a == b - float,float=bool
    LogicNotEqual, // Inequality: a != b - float,float=bool
    LogicLess, // Less than: a < b - float,float=bool
    LogicLessEqual, // Less than or equal: a <= b - float,float=bool
    LogicGreater, // Greater than: a > b - float,float=bool
    LogicGreaterEqual, // Greater than or equal: a >= b - float,float=bool
};

pub const In_Bool_Out_Bool = enum(i32) {
    LogicNot, // Logical NOT: !a - bool=bool
};

pub const In_Bool_Bool_Out_Bool = enum(i32) {
    LogicAnd, // Logical AND: a && b - bool,bool=bool
    LogicOr, // Logical OR: a || b - bool,bool=bool
};

pub const In_Text_TextAr_Out_ = enum(i32) {
    ExecuteCommand, // text, []text=void
};

pub const In_Text_Out_ = enum(i32) {
    Log, // text=void
};

pub const In_Text_Value_Out_ = enum(i32) {
    SetValueInt, // text, blockvalue=void
    SetValueFloat, // text, blockvalue=void
    SetValueBool, // text, blockvalue=void
    SetValueText, // text, blockvalue=void
    SetValueVector2, // text, blockvalue=void
};

pub const In_Out_Bool = enum(i32) {
    ReturnSuccess, // none=bool
    ReturnFailed, // none=bool
};

pub const BlockValueType = enum(i32) {
    null = 0,
    void,
    integer,
    float,
    boolean,
    text,
    text_array,
    path, // Value is the DR path, get the value and use it.  Allows a path to be used dynamically
    value, // Value is the value name.  This allows referencing value by name, so we can by more dynamic
    vector2,
    vector3,
    vector4,
    enumeration, // This uses the `int` as the Value and the `text` as the `Enum Type`, and then uses `get_enum_type.GlobalEnumInfo` to have all the names, and any type info for enum/tag functions
};

pub const BlockValue = struct {
    // Type determines the value stored
    type: BlockValueType = .null,

    // Name is used if this is a Named Value (like a var), otherwise not needed
    name: Text = Text.initEmpty(), // Every variable sent to the Block Stack becomes a NamedVariables, available as memory.  Only use the same names when you want to overwrite existing data, otherwise new names

    // Actual values
    integer: i32 = 0,
    float: f32 = 0.0,
    text: Text = Text.initEmpty(),
    boolean: bool = false,
    text_array: TextArray = TextArray.init(false),
    vec2: rl.Vector2 = .{},
    // vec3: rl.Vector3 = .{},
    // vec4: rl.Vector4 = .{},

    pub fn initVoid() BlockValue {
        return BlockValue{
            .type = .void,
        };
    }

    pub fn initInteger(value: ?i32) BlockValue {
        if (value == null) return .{ .type = .null };

        return BlockValue{
            .type = .integer,
            .integer = value.?,
        };
    }

    pub fn initFloat(value: ?f32) BlockValue {
        if (value == null) return .{ .type = .null };

        return BlockValue{
            .type = .float,
            .float = value.?,
        };
    }

    pub fn initText(value: ?Text) BlockValue {
        if (value == null) return .{ .type = .null };

        return BlockValue{
            .type = .text,
            .text = value.?,
        };
    }

    pub fn initBoolean(value: ?bool) BlockValue {
        if (value == null) return .{ .type = .null };

        return BlockValue{
            .type = .boolean,
            .boolean = value.?,
        };
    }

    pub fn initTextArray(value: ?TextArray) BlockValue {
        if (value == null) return .{ .type = .null };

        return BlockValue{
            .type = .text_array,
            .text_array = value.?,
        };
    }
};

pub const BlockInput = struct {
    type: BlockValueType = .void,

    // No reporter block to execute, we take the literal value
    literal_value: BlockValue = .{},

    // Single nested reporter block, id will be set to not -1 if used
    reporter_block: BlockRow = .{},

    // DR Path for this Block Row, so we can edit it.  This is childPath only, not the full path, so it can be cloned into a different record and still work.  _ prefix excludes from CreatePropPanel
    _edit_path: Text = Text.initEmpty(),
};

// Executor normally, and in the args (Reporter), its the same
pub const BlockRow = struct {
    id: i32 = -1, //TODO:REMOVE: `id` is not used, remove it
    type: BlockType = .None,

    inputs: []BlockInput = &[_]BlockInput{},
    child_rows: []BlockRow = &[_]BlockRow{},

    // The result of this row goes here, so it can be passed back as a Reporter for any of our types
    result: BlockValue = .{},

    // If not empty, set the value to the Value name, for use by other BlockRows
    set_result_to_value: Text = Text.initEmpty(),

    // DR Path for this Block Row, so we can edit it.  This is childPath only, not the full path, so it can be cloned into a different record and still work.  _ prefix excludes from CreatePropPanel
    _edit_path: Text = Text.initEmpty(),
};

pub const BlockStack = struct {
    id: i32 = -1, // Block Stack starts executing on 0.  0 is the entry BlockRow //TODO:REMOVE: `id` is not used, remove it
    name: Text = Text.initEmpty(),
    rows: []BlockRow = &[_]BlockRow{},
    values: []BlockValue = &[_]BlockValue{}, // Every variables we get is cached here, and can be used by later rows, for ease of reference.  No safety in the silo, just access
};

// ---- Structs only used in Commands, not in Data.  Never serialized: Start ----
pub const ExecutionContext = struct {
    // Used to track our Execution of a Block Stack
    entity_id: i32 = -1,
    delta_time: f32 = 0,

    // When not null, this gives us access to our Variables
    //NOTE: We cant be MemDB struct because of this, but this is important, and better we just
    block_stack: ?*BlockStack = null,

    // Trace
    trace: ?*EntityTrace = null,

    //NOTE: There is no output to an BlockStack, my entire system is a state system, I change something in DR, thats it.  Everything is in DR.  There is only 1 place.  There is only Working Space and DR
    result: BlockValue = .{},

    // Location
    current_row_index: i32 = 0,
    skip_to_row_index: i32 = -1,
    error_message: Text = Text.init(""),
};
// ---- Structs only used in Commands, not in Data.  Never serialized: End ----

var global_block_row_id: i32 = 0;
pub fn generateBlockRowId() i32 {
    global_block_row_id += 1;
    return global_block_row_id;
}

var global_block_stack_id: i32 = 0;
pub fn generateBlockStackId() i32 {
    global_block_stack_id += 1;
    return global_block_stack_id;
}
