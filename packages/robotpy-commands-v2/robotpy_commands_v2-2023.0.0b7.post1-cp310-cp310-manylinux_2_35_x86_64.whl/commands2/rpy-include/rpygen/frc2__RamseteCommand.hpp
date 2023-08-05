
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <../src/include/frc2/command/RamseteCommand.h>




#include <rpygen/frc2__CommandBase.hpp>

namespace rpygen {

using namespace frc2;


template <typename CfgBase>
using PyTrampolineCfgBase_frc2__RamseteCommand =
    PyTrampolineCfg_frc2__CommandBase<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_frc2__RamseteCommand :
    PyTrampolineCfgBase_frc2__RamseteCommand< CfgBase>
{
    using Base = frc2::RamseteCommand;

    using override_base_Initialize_v = frc2::RamseteCommand;
    using override_base_Execute_v = frc2::RamseteCommand;
    using override_base_End_b = frc2::RamseteCommand;
    using override_base_IsFinished_v = frc2::RamseteCommand;
    using override_base_InitSendable_RTSendableBuilder = frc2::RamseteCommand;
};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_frc2__RamseteCommand =
    PyTrampoline_frc2__CommandBase<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_frc2__RamseteCommand : PyTrampolineBase_frc2__RamseteCommand<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_frc2__RamseteCommand<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_frc2__RamseteCommand;



#ifndef RPYGEN_DISABLE_Initialize_v
    void Initialize() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_Initialize_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "initialize", );
        return CxxCallBase::Initialize();
    }
#endif

#ifndef RPYGEN_DISABLE_Execute_v
    void Execute() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_Execute_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "execute", );
        return CxxCallBase::Execute();
    }
#endif

#ifndef RPYGEN_DISABLE_End_b
    void End(bool interrupted) override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_End_b;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "end", interrupted);
        return CxxCallBase::End(std::move(interrupted));
    }
#endif

#ifndef RPYGEN_DISABLE_IsFinished_v
    bool IsFinished() override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_IsFinished_v;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(bool), LookupBase,
            "isFinished", );
        return CxxCallBase::IsFinished();
    }
#endif

#ifndef RPYGEN_DISABLE_InitSendable_RTSendableBuilder
    void InitSendable(wpi::SendableBuilder& builder) override {
        using LookupBase = typename PyTrampolineCfg::Base;
        using CxxCallBase = typename PyTrampolineCfg::override_base_InitSendable_RTSendableBuilder;
        PYBIND11_OVERRIDE_IMPL(PYBIND11_TYPE(void), LookupBase,
            "initSendable", builder);
        return CxxCallBase::InitSendable(std::forward<decltype(builder)>(builder));
    }
#endif




};

}; // namespace rpygen
