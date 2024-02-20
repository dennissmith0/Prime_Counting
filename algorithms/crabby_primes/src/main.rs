#![feature(portable_simd)]

use clap::Parser;
// use range_set_blaze::RangeSetBlaze;
// use rayon::iter::{IntoParallelRefIterator, ParallelIterator};

#[derive(Debug, Clone, Parser)]
pub struct Cli {
    #[arg(short = 'n', default_value = "1_000_000")]
    pub n: u32,
}

fn main() {
    let cli: Cli = Cli::parse();

    println!("Running PNT w/ n = {}", cli.n);

    let x = create_and_count(cli.n);

    println!("The result is: {x}");
}

fn create_and_count(n: u32) -> u32 {
    let deltas: [i32; 2] = [-1, 1];
    let mut poss = vec![];

    let first_part = std::time::Instant::now();

    for (count, val) in (6..n + 1).step_by(6).enumerate() {
        for delta in &deltas {
            match delta.cmp(&0) {
                std::cmp::Ordering::Less => {
                    poss.push((count, val - 1));
                }
                std::cmp::Ordering::Greater => {
                    poss.push((count, val + 1));
                }
                _ => unreachable!(),
            }
        }
    }

    eprintln!("Firt part took: {:?}", first_part.elapsed());

    let mult: std::collections::BTreeSet<u32> = poss
        .iter()
        .flat_map(|&(idx, i)| {
            poss[idx..].iter().map_while(move |(_, j)| {
                let product = i * j;
                if product <= n {
                    Some(product)
                } else {
                    None
                }
            })
        })
        .collect();
    // .collect::<RangeSetBlaze<i32>>();

    poss.len() as u32 - mult.len() as u32 + 2_u32
}
