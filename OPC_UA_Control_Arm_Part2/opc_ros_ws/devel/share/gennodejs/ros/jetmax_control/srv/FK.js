// Auto-generated. Do not edit!

// (in-package jetmax_control.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class FKRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.angle_rotate = null;
      this.angle_left = null;
      this.angle_right = null;
    }
    else {
      if (initObj.hasOwnProperty('angle_rotate')) {
        this.angle_rotate = initObj.angle_rotate
      }
      else {
        this.angle_rotate = 0.0;
      }
      if (initObj.hasOwnProperty('angle_left')) {
        this.angle_left = initObj.angle_left
      }
      else {
        this.angle_left = 0.0;
      }
      if (initObj.hasOwnProperty('angle_right')) {
        this.angle_right = initObj.angle_right
      }
      else {
        this.angle_right = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FKRequest
    // Serialize message field [angle_rotate]
    bufferOffset = _serializer.float64(obj.angle_rotate, buffer, bufferOffset);
    // Serialize message field [angle_left]
    bufferOffset = _serializer.float64(obj.angle_left, buffer, bufferOffset);
    // Serialize message field [angle_right]
    bufferOffset = _serializer.float64(obj.angle_right, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FKRequest
    let len;
    let data = new FKRequest(null);
    // Deserialize message field [angle_rotate]
    data.angle_rotate = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [angle_left]
    data.angle_left = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [angle_right]
    data.angle_right = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'jetmax_control/FKRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bc78582ee0d138ee3fa007868686f159';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 angle_rotate
    float64 angle_left
    float64 angle_right
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FKRequest(null);
    if (msg.angle_rotate !== undefined) {
      resolved.angle_rotate = msg.angle_rotate;
    }
    else {
      resolved.angle_rotate = 0.0
    }

    if (msg.angle_left !== undefined) {
      resolved.angle_left = msg.angle_left;
    }
    else {
      resolved.angle_left = 0.0
    }

    if (msg.angle_right !== undefined) {
      resolved.angle_right = msg.angle_right;
    }
    else {
      resolved.angle_right = 0.0
    }

    return resolved;
    }
};

class FKResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FKResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FKResponse
    let len;
    let data = new FKResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'jetmax_control/FKResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FKResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: FKRequest,
  Response: FKResponse,
  md5sum() { return 'dc592708003b91537cff0bcafe06c7d7'; },
  datatype() { return 'jetmax_control/FK'; }
};
