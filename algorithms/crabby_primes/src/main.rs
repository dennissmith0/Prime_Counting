use std::collections::BTreeSet;
use std::sync::Arc;
use std::thread;

use clap::Parser;

#[derive(Debug, Clone, Parser)]
pub struct Cli {
    #[arg(short = 'n', default_value = "1_000_000")]
    pub n: i32,
}

fn main() {
    let cli: Cli = Cli::parse();

    println!("Running PNT w/ n = {}", cli.n);

    let x = create_and_count(cli.n);

    println!("The result is: {x}");
}

fn create_and_count(n: i32) -> u64 {
    let deltas: [i32; 2] = [-1, 1];
    let mut poss = vec![];
    for (count, val) in (6..n + 1).step_by(6).enumerate() {
        for &delta in &deltas {
            poss.push((count, val + delta));
        }
    }
    let poss = Arc::new(poss);

    let mut mult: BTreeSet<i32> = BTreeSet::new();

    let threads = num_cpus::get() - 1; // Get the number of CPUs
    let mut handles = vec![];

    let chunk_size = poss.len() / threads;

    for i in 0..threads {
        let poss = Arc::clone(&poss);
        let handle = thread::spawn(move || {
            let start = chunk_size * i;
            let end = if i == threads - 1 {
                poss.len()
            } else {
                start + chunk_size
            };

            poss[start..end]
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
                .collect::<BTreeSet<_>>()
        });
        handles.push(handle);
    }

    for handle in handles {
        let hs = handle.join().unwrap();
        mult.extend(&hs);
    }

    (poss.len() - mult.len() + 2) as u64
}
