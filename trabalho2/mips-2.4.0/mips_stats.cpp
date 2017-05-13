/******************************************************
 * ArchC Processor statistics data implementation file. *
 * This file is automatically generated by ArchC      *
 * WITHOUT WARRANTY OF ANY KIND, either express       *
 * or implied.                                        *
 * For more information on ArchC, please visit:       *
 * http://www.archc.org                               *
 *                                                    *
 * The ArchC Team                                     *
 * Computer Systems Laboratory (LSC)                  *
 * IC-UNICAMP                                         *
 * http://www.lsc.ic.unicamp.br                       *
 ******************************************************/
 

#include "mips_stats.H"

AC_CONF_STAT_LIST(mips, INSTRUCTIONS, SYSCALLS);
AC_CONF_INSTR_STAT_LIST(mips, COUNT);

mips_all_stats::mips_all_stats() :
  stats("mips")
  , lb_istats("lb", stats)
  , lbu_istats("lbu", stats)
  , lh_istats("lh", stats)
  , lhu_istats("lhu", stats)
  , lw_istats("lw", stats)
  , lwl_istats("lwl", stats)
  , lwr_istats("lwr", stats)
  , sb_istats("sb", stats)
  , sh_istats("sh", stats)
  , sw_istats("sw", stats)
  , swl_istats("swl", stats)
  , swr_istats("swr", stats)
  , addi_istats("addi", stats)
  , addiu_istats("addiu", stats)
  , slti_istats("slti", stats)
  , sltiu_istats("sltiu", stats)
  , andi_istats("andi", stats)
  , ori_istats("ori", stats)
  , xori_istats("xori", stats)
  , lui_istats("lui", stats)
  , add_istats("add", stats)
  , addu_istats("addu", stats)
  , sub_istats("sub", stats)
  , subu_istats("subu", stats)
  , slt_istats("slt", stats)
  , sltu_istats("sltu", stats)
  , instr_and_istats("instr_and", stats)
  , instr_or_istats("instr_or", stats)
  , instr_xor_istats("instr_xor", stats)
  , instr_nor_istats("instr_nor", stats)
  , nop_istats("nop", stats)
  , sll_istats("sll", stats)
  , srl_istats("srl", stats)
  , sra_istats("sra", stats)
  , sllv_istats("sllv", stats)
  , srlv_istats("srlv", stats)
  , srav_istats("srav", stats)
  , mult_istats("mult", stats)
  , multu_istats("multu", stats)
  , div_istats("div", stats)
  , divu_istats("divu", stats)
  , mfhi_istats("mfhi", stats)
  , mthi_istats("mthi", stats)
  , mflo_istats("mflo", stats)
  , mtlo_istats("mtlo", stats)
  , j_istats("j", stats)
  , jal_istats("jal", stats)
  , jr_istats("jr", stats)
  , jalr_istats("jalr", stats)
  , beq_istats("beq", stats)
  , bne_istats("bne", stats)
  , blez_istats("blez", stats)
  , bgtz_istats("bgtz", stats)
  , bltz_istats("bltz", stats)
  , bgez_istats("bgez", stats)
  , bltzal_istats("bltzal", stats)
  , bgezal_istats("bgezal", stats)
  , sys_call_istats("sys_call", stats)
  , instr_break_istats("instr_break", stats)
{
    //!Configuring stats collectors for each instruction
    instr_stats[1] = &lb_istats;
    instr_stats[2] = &lbu_istats;
    instr_stats[3] = &lh_istats;
    instr_stats[4] = &lhu_istats;
    instr_stats[5] = &lw_istats;
    instr_stats[6] = &lwl_istats;
    instr_stats[7] = &lwr_istats;
    instr_stats[8] = &sb_istats;
    instr_stats[9] = &sh_istats;
    instr_stats[10] = &sw_istats;
    instr_stats[11] = &swl_istats;
    instr_stats[12] = &swr_istats;
    instr_stats[13] = &addi_istats;
    instr_stats[14] = &addiu_istats;
    instr_stats[15] = &slti_istats;
    instr_stats[16] = &sltiu_istats;
    instr_stats[17] = &andi_istats;
    instr_stats[18] = &ori_istats;
    instr_stats[19] = &xori_istats;
    instr_stats[20] = &lui_istats;
    instr_stats[21] = &add_istats;
    instr_stats[22] = &addu_istats;
    instr_stats[23] = &sub_istats;
    instr_stats[24] = &subu_istats;
    instr_stats[25] = &slt_istats;
    instr_stats[26] = &sltu_istats;
    instr_stats[27] = &instr_and_istats;
    instr_stats[28] = &instr_or_istats;
    instr_stats[29] = &instr_xor_istats;
    instr_stats[30] = &instr_nor_istats;
    instr_stats[31] = &nop_istats;
    instr_stats[32] = &sll_istats;
    instr_stats[33] = &srl_istats;
    instr_stats[34] = &sra_istats;
    instr_stats[35] = &sllv_istats;
    instr_stats[36] = &srlv_istats;
    instr_stats[37] = &srav_istats;
    instr_stats[38] = &mult_istats;
    instr_stats[39] = &multu_istats;
    instr_stats[40] = &div_istats;
    instr_stats[41] = &divu_istats;
    instr_stats[42] = &mfhi_istats;
    instr_stats[43] = &mthi_istats;
    instr_stats[44] = &mflo_istats;
    instr_stats[45] = &mtlo_istats;
    instr_stats[46] = &j_istats;
    instr_stats[47] = &jal_istats;
    instr_stats[48] = &jr_istats;
    instr_stats[49] = &jalr_istats;
    instr_stats[50] = &beq_istats;
    instr_stats[51] = &bne_istats;
    instr_stats[52] = &blez_istats;
    instr_stats[53] = &bgtz_istats;
    instr_stats[54] = &bltz_istats;
    instr_stats[55] = &bgez_istats;
    instr_stats[56] = &bltzal_istats;
    instr_stats[57] = &bgezal_istats;
    instr_stats[58] = &sys_call_istats;
    instr_stats[59] = &instr_break_istats;
}