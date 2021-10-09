/**
 * @file pin_configuration.hpp
 * @author Mergim Halimi (m.halimi123@gmail.com)
 * @brief
 * @version 0.1
 * @date 2021-10-09
 *
 * @copyright Copyright (c) 2021, mhRobotics, Inc., All rights reserved.
 *
 */
#ifndef CAN_ATMEGA328P_SRC_PIN_CONFIGURATION_HPP_
#define CAN_ATMEGA328P_SRC_PIN_CONFIGURATION_HPP_

typedef struct PinConfiguration {
  uint8_t motor_brake;
  uint8_t motor_enable;
  uint8_t motor_signal;
  uint8_t motor_direction;
  uint8_t motor_speed;

  uint8_t can_mcp_irq;
  uint8_t can_mcp_rcv;
  uint8_t can_mcp_mosi;
  uint8_t can_mcp_miso;
  uint8_t can_mcp_sck;

  uint8_t wheel_front_left;
  uint8_t wheel_front_right;
  uint8_t wheel_back_left;
  uint8_t wheel_back_right;

  PinConfiguration()
      : motor_brake{PD7}, motor_enable{PD4}, motor_signal{PD3},
        motor_direction{PD5}, motor_speed{PD6}, can_mcp_irq{PD2},
        can_mcp_rcv{PB2}, can_mcp_mosi{PB3}, can_mcp_miso{PB4},
        can_mcp_sck{PB5}, wheel_front_left{PC0}, wheel_front_right{PC1},
        wheel_back_left{PC2}, wheel_back_right{PC3} {}

  PinConfiguration(uint8_t motorBrake, uint8_t motorEnable, uint8_t motorSignal,
                   uint8_t motorDirection, uint8_t motorSpeed,
                   uint8_t canMcpIrq, uint8_t canMcpRcv, uint8_t canMcpMosi,
                   uint8_t canMcpMiso, uint8_t canMcpSck,
                   uint8_t wheelFrontLeft, uint8_t wheelFrontRight,
                   uint8_t wheelBackLeft, uint8_t wheelBackRight)
      : motor_brake{motorBrake}, motor_enable{motorEnable},
        motor_signal{motorSignal}, motor_direction{motorDirection},
        motor_speed{motorSpeed}, can_mcp_irq{canMcpIrq}, can_mcp_rcv{canMcpRcv},
        can_mcp_mosi{canMcpMosi}, can_mcp_miso{canMcpMiso},
        can_mcp_sck{canMcpSck}, wheel_front_left{wheelFrontLeft},
        wheel_front_right{wheelFrontRight}, wheel_back_left{wheelBackLeft},
        wheel_back_right{wheelBackRight} {}
} pin_configuration_t;

#define SPEED_CONTROL_PWM(speed) ((OCR0A) = (speed))
#define DIRECTION_BIT_INDEX 6
#define SPEED_BIT_INDEX 7

constexpr int kTimeoutMs = 250;

#include "drivers/include/millis.h"
#include "drivers/include/spi.h"
#include "drivers/include/usart.h"

#endif // CAN_ATMEGA328P_SRC_PIN_CONFIGURATION_HPP_
