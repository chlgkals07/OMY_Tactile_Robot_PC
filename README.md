# OMY_Tactile_Robot_PC

SHAPE-UP Tactile 프로젝트의 **Robot PC(OMY 내부 PC, ROS 2 Jazzy 컨테이너)** 쪽 코드.
User PC 쪽 코드는 `SHAPE_UP_Tactile` 레포의 `user_pc/`에 있다.

## 원칙
- ROBOTIS `open_manipulator`는 **수정하지 않는다.** 이 레포는 기존 설치 위에 얹는(overlay) ROS 2 패키지만 둔다.
- 공식 `omy_ai.launch.py`가 그리퍼 제거 상태에서 정상 동작하면 이 레포의 패키지는 필요 없다.

## 배경
OMY의 leader–follower 텔레옵은 Robot PC 안에서 닫힌다.
- leader(`omy_l100_leader_ai.launch.py`)가 `/leader/joint_trajectory`를 publish한다 (7관절: `joint1~6`, `rh_r1_joint`).
- follower(`omy_f3m_follower_ai.launch.py`)가 이 토픽을 구독한다.
- 그리퍼(`OMYF3MEndUnitSystem`, 포트 `/dev/ttyAMA4`, Dynamixel ID 7)를 떼면 공식 launch가 실패할 것으로 추정된다 (미확인).

해결 방침: 팔은 실제 하드웨어, end unit 시스템만 `use_mock_hardware`로 두어 `rh_r1_joint`를 가상 관절로 유지한다.
설계 전문: `SHAPE_UP_Tactile/docs/superpowers/specs/2026-10-08-leap-omy-teleop-design.md`

## 두 레포 사이의 계약
- 토픽: `/leader/joint_trajectory` (`trajectory_msgs/JointTrajectory`)
- 관절 이름: `rh_r1_joint`
- `ROS_DOMAIN_ID=30`

## 상태
패키지 `omy_leap_bringup`은 공식 launch가 실패한 것을 확인한 뒤 추가한다 (계획서 Task 13).
